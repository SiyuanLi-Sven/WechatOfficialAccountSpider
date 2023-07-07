# get_params.py
from mitmproxy import io
from mitmproxy.exceptions import FlowReadException
import re
import os


# command: python get_params outfile
def get_params(outfile):
    with open(outfile, "rb") as logfile:
        freader = io.FlowReader(logfile)
        try:
            for f in freader.stream():
                # 获取完整的请求信息
                state = f.get_state()
                # 尝试获取cookie和appmsg_token,如果成功就停止
                try:
                    # 截取其中request部分
                    request = state["request"]
                    # 提取Cookie
                    for item in request["headers"]:
                        key, value = item
                        if key == b"Cookie":
                            cookie = value.decode()

                    # 提取appmsg_token
                    path = request["path"].decode()
                    appmsg_token_string = re.findall("appmsg_token.+?&", path)
                    appmsg_token = appmsg_token_string[0].split("=")[1][:-1]
                    break
                except Exception:
                    continue
        except FlowReadException as e:
            print("Flow file corrupted: {}".format(e))
    return appmsg_token, cookie


def main(outfile):
    path = os.path.split(os.path.realpath(__file__))[0]
    command = "mitmdump -q -s {}/get_outfile.py -w {} mp.weixin.qq.com/mp/getappmsgext".format(
        path, outfile)
    os.system(command)
    try:
        os.system("rm ./-q")
    except Exception:
        pass
    return get_params(outfile)


# coding: utf-8
# get_outfile.py
import urllib
import sys
from mitmproxy import io, http


# 使用命令行过滤规则
# command: mitmdump -s get_outfile.py -w outfile mp.weixin.qq.com/mp/getappmsgext
class Writer:
    def __init__(self, path: str) -> None:
        self.f = open(path, "wb")
        self.w = io.FlowWriter(self.f)

    def response(self, flow: http.HTTPFlow) -> None:
        self.w.add(flow)
        url = urllib.parse.unquote(flow.request.url)
        if "mp.weixin.qq.com/mp/getappmsgext" in url:
            exit()

    def done(self):

        self.f.close()


addons = [Writer(sys.argv[1])]