import os
import dpkt
import socket
import datetime
import uuid

from scapy.sendrecv import sniff
from scapy.utils import wrpcap

def get_local_ip():

    hostname = socket.gethostname()
    # 获取本机内网ip
    local_ips = socket.gethostbyname_ex(hostname)[-1]

    return local_ips

def body_transfer(body):

    str_body = body.decode()

    body_ls = str_body.split("&")

    for item in body_ls:
        key_, value_ = item.split("=")
        print("   %s: %s"% (key_, value_))

def get_dpkt():

    dpkt_ = sniff(count = 100，iface='Qualcomm QCA9377 802.11ac Wireless Adapter')  #这里是针对单网卡的机子，多网卡的可以在参数中指定网卡,例：iface=Qualcomm QCA9377 802.11ac Wireless Adapter
    _uuid = uuid.uuid1()
    filename = f"{_uuid}.pcap"
    wrpcap(filename, dpkt_)

    return filename

def print_pcap(pcap):
    try:
        local_ips = get_local_ip()

        for timestamp, buf in pcap:
            eth = dpkt.ethernet.Ethernet(buf) #获得以太包，即数据链路层包
            # print("ip layer:"+eth.data.__class__.__name__) #以太包的数据既是网络层包
            # print("tcp layer:"+eth.data.data.__class__.__name__) #网络层包的数据既是传输层包
            # print("http layer:" + eth.data.data.data.__class__.__name__) #传输层包的数据既是应用层包
            #
            # print('Timestamp: ',str(datetime.datetime.utcfromtimestamp(timestamp))) #打印出包的抓取时间

            if not isinstance(eth.data, dpkt.ip.IP):
                print('Non IP Packet type not supported %s' % eth.data.__class__.__name__)
                continue
            ip = eth.data
            src_ip = socket.inet_ntoa(ip.src)
            dst_ip = socket.inet_ntoa(ip.dst)
            do_not_fragment =bool(ip.off & dpkt.ip.IP_DF)
            more_fragments =bool(ip.off & dpkt.ip.IP_MF)
            fragment_offset = ip.off & dpkt.ip.IP_OFFMASK

            if isinstance(ip.data, dpkt.tcp.TCP):

                # Set the TCP data
                tcp = ip.data

                # Now see if we can parse the contents as a HTTP request
                # 看看是否可以将内容解析为HTTP请求
                try:

                    request = dpkt.http.Request(tcp.data)

                    print('IP: %s -> %s (len=%d ttl=%d DF=%d MF=%d offset=%d)' % (src_ip + "(本机)" if src_ip in local_ips else src_ip, dst_ip, ip.len, ip.ttl, do_not_fragment, more_fragments,fragment_offset))

                    print("URL: %s" % request.headers.get("host") + request.uri)
                    print("METHOD: %s" % request.method.upper())
                    print("Headers: ")
                    for key, value in request.headers.items():
                        print("   %s: %s" %(key, value))

                    print("Body:")
                    body_transfer(request.body)
                    print("Data:")
                    body_transfer(request.data)
                    # print('HTTP request: %s\n' % repr(request))

                    print()
                except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
                    continue

                # Pull out fragment information (flags and offset all packed into off field, so use bitmasks)

    except Exception as error:
        pass

def main():

    while True:
        filename = get_dpkt()
        with open(filename, "rb") as f:
            pcap = dpkt.pcap.Reader(f)
            print_pcap(pcap)

        os.remove(filename)

if __name__ =='__main__':
    main()