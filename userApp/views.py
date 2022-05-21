import re

from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
# HttpResponse
def index(request):
    return render(request, 'index.html', {'news': getnews()})


def users(request):
    # 默认会去templates寻找html
    # AccountID=0&Guid=0&RoleName=

    return render(request, 'users.html')


def news(request):
    tp = getnews()
    return render(request, 'news.html', {'news': tp})


def cdx(request):
    return redirect('https://www.baidu.com/')


def xwxq(request):
    cp_id = request.GET.get("id")
    return render(request, "xwxq.html", getnews(int(cp_id)))


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    uses = request.POST.get("user")
    pwd = request.POST.get("pw")
    if uses == "1" and pwd == "1":
        return HttpResponse("登录成功")
    return render(request, "login.html", {'tip': "登录错误"})


# 公司简介模板
def gsjj(request):
    return render(request, "gsjj.html")


def gszs(request):
    return render(request, "gszs.html")


def lxwm(request):
    return render(request, "lxwm.html")


def mymap(request):
    return render(request, "mymap.html")


def cpzx(request):
    # MTC模块数据
    jianjie = "椿树固态继电器它可以实现用微弱的控制信号（几毫安到几十毫安）控制0.1A直到几百A电流负载，进行无触点接通或分断。固态继电器工" \
              "作可靠，无触点、无火花、寿命长、无噪声，无电磁干扰，开关速度快，抗干扰能力强，且体积小" \
              "，耐振动，耐冲击，防爆、防潮、防腐蚀、能与TTL、DTL、HTL等逻辑电路兼容。"

    # 型号 图片 连接 /static/img/20060Q11536.jpg
    cp_id = request.GET.get("id")
    s = {'cp_url': cp_id, 'cp_name': '', 'mklist': ''}
    if cp_id == "mokuai":
        mtc = {'name': 'MTC模块', 'jianjie': jianjie, "list": getmtclist(), 'dir': 'mtc'}
        mdc = {'name': 'MDC模块', 'jianjie': jianjie, "list": getmdclist(), 'dir': 'mdc'}
        mda = {'name': 'MDA模块', 'jianjie': jianjie, "list": getmdalist(), 'dir': 'mda'}
        mdk = {'name': 'MDK模块', 'jianjie': jianjie, "list": getmdklist(), 'dir': 'mdk'}
        mta = {'name': 'MTA模块', 'jianjie': jianjie, "list": getmtalist(), 'dir': 'mta'}
        mtk = {'name': 'MTK模块', 'jianjie': jianjie, "list": getmtklist(), 'dir': 'mtk'}
        mtx = {'name': 'MTX模块', 'jianjie': jianjie, "list": getmtxlist(), 'dir': 'mtx'}
        mfc = {'name': 'MFC模块', 'jianjie': jianjie, "list": getmfclist(), 'dir': 'mfc'}
        mfa = {'name': 'MFA模块', 'jianjie': jianjie, "list": getmfalist(), 'dir': 'mfa'}
        md = {'name': 'MD模块', 'jianjie': jianjie, "list": getmdlist(), 'dir': 'md'}
        mlist = [mtc, mdc, mda, mdk, mfc, mfa, mtx, md, mta, mtk]
        s['cp_name'], s['mklist'] = '模块系列', mlist

    # 固态继电器
    elif cp_id == "gtjdq":
        ssrad = {'name': 'SSR-DA-直流控制交流固态继电器', 'jianjie': jianjie, "list": getssrda(), 'dir': 'ssrad'}
        ssrva = {'name': 'SSR-VA-调压器-固态继电器', 'jianjie': jianjie, "list": getssrva(), 'dir': 'ssrva'}
        ssrdd = {'name': 'SSR-DD-直流控制直流-固态继电器', 'jianjie': jianjie, "list": getssrdd(), 'dir': 'ssrdd'}
        ssraa = {'name': 'SSR-AA-交流控制交流-固态继电器', 'jianjie': jianjie, "list": getssraa(), 'dir': 'ssraa'}
        jgxda = {'name': 'JGX-3 DA-直流控制交流-三相固态继电器', 'jianjie': jianjie, "list": getjgxda(), 'dir': 'jgxda'}
        jgxaa = {'name': 'JGX-3 AA-交流控制交流-三相固态继电器', 'jianjie': jianjie, "list": getjgxaa(), 'dir': 'jgxaa'}

        mlist = [ssrad, ssrva, ssraa, ssrdd, jgxda, jgxaa]
        s['cp_name'], s['mklist'] = '固态继电器', mlist

    elif cp_id == "luoxuan":

        kp = {'name': 'KP螺旋-晶闸管', 'jianjie': jianjie, "list": getkplx(), 'dir': 'kplx'}
        zp = {'name': 'ZP螺旋-二极管', 'jianjie': jianjie, "list": getzplx(), 'dir': 'zplx'}
        ks = {'name': 'KS螺旋-双向晶闸管', 'jianjie': jianjie, "list": getkslx(), 'dir': 'kslx'}
        zk = {'name': 'ZK螺旋-普通整流管', 'jianjie': jianjie, "list": getzklx(), 'dir': 'lxzk'}
        mlist = [kp, zp, ks, zk]
        s['cp_name'], s['mklist'] = '螺旋系列', mlist
    elif cp_id == "pingban":
        kp = {'name': 'KP平板晶闸管', 'jianjie': jianjie, "list": getkppb(), 'dir': 'kppb'}
        zp = {'name': 'ZP平板二极管', 'jianjie': jianjie, "list": getzppb(), 'dir': 'zppb'}
        ks = {'name': 'KS双向晶闸管', 'jianjie': jianjie, "list": getkspb(), 'dir': 'kspb'}
        zk = {'name': 'ZK普通整流管', 'jianjie': jianjie, "list": getzkpb(), 'dir': 'zkpb'}
        kk = {'name': 'KK高频晶闸管', 'jianjie': jianjie, "list": getkkpb(), 'dir': 'kkpb'}
        ka = {'name': 'KA快速晶闸管', 'jianjie': jianjie, "list": getkapb(), 'dir': 'kapb'}
        mlist = [kp, zp, ks, kk, zk, ka]
        s['cp_name'], s['mklist'] = '平板系列', mlist
    elif cp_id == "zlq":
        mdq = {'name': 'MDQ单相整流模块', 'jianjie': jianjie, "list": getmdq(), 'dir': 'mdq'}
        mds = {'name': 'MDS三相整流模块', 'jianjie': jianjie, "list": getmds(), 'dir': 'mds'}
        sql = {'name': 'SQL三相整流桥', 'jianjie': jianjie, "list": getsql(), 'dir': 'sql'}
        ql = {'name': 'QL单相整流桥', 'jianjie': jianjie, "list": getql(), 'dir': 'ql'}
        kbpc = {'name': 'KBPC整流桥', 'jianjie': jianjie, "list": getkbpc(), 'dir': 'kbpc'}
        fzq = {'name': '4ZQ整流桥', 'jianjie': jianjie, "list": getfzq(), 'dir': '4zq'}
        mfq = {'name': 'MFQ整流模块', 'jianjie': jianjie, "list": getmfq(), 'dir': 'mfq'}
        mdst = {'name': 'MDST半波整流模块', 'jianjie': jianjie, "list": getmdst(), 'dir': 'mdst'}
        mlist = [mdq, mds, sql, ql, kbpc, fzq, mfq, mdst]
        s['cp_name'], s['mklist'] = '整流桥系列', mlist
    elif cp_id == "srq":
        sf = {'name': 'SF风冷散热器', 'jianjie': jianjie, "list": getsf(), 'dir': 'sf'}
        ss = {'name': 'SS水冷散热器', 'jianjie': jianjie, "list": getss(), 'dir': 'ss'}
        lxsr = {'name': '螺旋散热器', 'jianjie': jianjie, "list": getlxsr(), 'dir': 'lxsr'}
        mlist = [sf, ss, lxsr]
        s['cp_name'], s['mklist'] = '散热器系列', mlist
    elif cp_id == "cpfj":
        fj = {'name': '风机', 'jianjie': jianjie, "list": getfj(), 'dir': 'fj'}
        cfq = {'name': '模块触发器', 'jianjie': jianjie, "list": getcfq(), 'dir': 'cfq'}
        mlist = [fj, cfq]
        s['cp_name'], s['mklist'] = '散热器系列', mlist
    elif cp_id == "gyjgtjdq":
        gyjgtjdq = {'name': '工业级固态继电器', 'jianjie': jianjie, "list": getgyjgtjdq(), 'dir': 'gyjgtjdq'}
        mlist = [gyjgtjdq]
        s['cp_name'], s['mklist'] = '工业级固态继电器', mlist

    return render(request, "cpzx.html", s)


def cpxq(request):
    cp_id = request.GET.get("id").upper()
    # MTC类 散热器图片散热器链接
    sanre = [{'img': 'sanre.jpg', 'url': 'url'},
             {'img': 'sanre.jpg', 'url': 'url'}]
    s = {'name': cp_id, 'list': '', 'shipin': 'aid=927940107&amp;bvid=BV1iK4y1f7uQ&amp;cid=261919088&amp;page=18',
         'sanre': sanre, 'sj': 'mokuai', 'dir': '25', 'abs': 'mtc'}
    if 'MTC' in cp_id:
        s['list'], swithc = getmtclist(), getmtclist(2)
        s['dir'] = swithc[cp_id]
    elif 'MD' == cp_id or re.search('MD\\d+', cp_id) is not None:
        s['list'], swithc = getmdlist(), getmdlist(2)
        s['dir'], s['abs'] = swithc[cp_id], 'md'
    elif 'MDC' in cp_id:
        s['list'], swithc = getmdclist(), getmdclist(2)
        s['dir'], s['abs'] = swithc[cp_id], 'mdc'
    elif 'MDA' in cp_id:
        s['list'], swithc = getmdalist(), getmdalist(2)
        s['dir'], s['abs'] = swithc[cp_id], 'mda'
    elif 'MDK' in cp_id:
        s['list'], swithc = getmdklist(), getmdklist(2)
        s['dir'], s['abs'] = swithc[cp_id], 'mdk'
    elif 'MFC' in cp_id:
        s['list'], swithc = getmfclist(), getmfclist(2)
        s['dir'], s['abs'] = swithc[cp_id], 'mfc'
    elif 'MFA' in cp_id:
        s['list'], swithc = getmfclist(), getmfclist(2)
        s['dir'], s['abs'] = swithc[cp_id], 'mfa'
    elif 'MTA' in cp_id:
        s['list'], swithc = getmtalist(), getmtalist(2)
        s['dir'], s['abs'] = swithc[cp_id], 'mta'
    elif 'MTK' in cp_id:
        s['list'], swithc = getmtklist(), getmtklist(2)
        s['dir'], s['abs'] = swithc[cp_id], 'mtk'
    elif 'MTX' in cp_id:
        s['list'], swithc = getmtxlist(), getmtxlist(2)
        s['dir'], s['abs'] = swithc[cp_id], 'mtx'
    elif re.search('SSR\\d+DA', cp_id) is not None:
        s['list'], swithc = getssrda(), getssrda(2)
        s['dir'], s['abs'] = swithc[cp_id], 'ssrda'
    elif re.search('SSR\\d+AA', cp_id) is not None:
        s['list'], swithc = getssraa(), getssraa(2)
        s['dir'], s['abs'] = swithc[cp_id], 'ssraa'
    elif re.search('SSR\\d+VA', cp_id) is not None:
        s['list'], swithc = getssrva(), getssrva(2)
        s['dir'], s['abs'] = swithc[cp_id], 'ssrva'
    elif re.search('SSR\\d+DD', cp_id) is not None:
        s['list'], swithc = getssrdd(), getssrdd(2)
        s['dir'], s['abs'] = swithc[cp_id], 'ssrdd'
    elif re.search('JGX-3 \\d+DA', cp_id) is not None:
        s['list'], swithc = getjgxda(), getjgxda(2)
        s['dir'], s['abs'] = swithc[cp_id], 'jgxda'
    elif re.search('JGX-3 \\d+AA', cp_id) is not None:
        s['list'], swithc = getssraa(), getssraa(2)
        s['dir'], s['abs'] = swithc[cp_id], 'jgxaa'
    elif re.search('KP\\d+A\(', cp_id) is not None:
        s['list'], swithc = getkppb(), getkppb(2)
        s['dir'], s['abs'] = swithc[cp_id], 'kppb'
    elif re.search('ZP\\d+A\(', cp_id) is not None:
        s['list'], swithc = getzppb(), getzppb(2)
        s['dir'], s['abs'] = swithc[cp_id], 'zppb'
    elif re.search('KS\\d+A\(', cp_id) is not None:
        s['list'], swithc = getkspb(), getkspb(2)
        s['dir'], s['abs'] = swithc[cp_id], 'kspb'
    elif re.search('KK\\d+A\(', cp_id) is not None:
        s['list'], swithc = getkkpb(), getkkpb(2)
        s['dir'], s['abs'] = swithc[cp_id], 'kkpb'
    elif re.search('ZK\\d+A\(', cp_id) is not None:
        s['list'], swithc = getzkpb(), getzkpb(2)
        s['dir'], s['abs'] = swithc[cp_id], 'zkpb'
    elif re.search('KA\\d+A\(', cp_id) is not None:
        s['list'], swithc = getkapb(), getkapb(2)
        s['dir'], s['abs'] = swithc[cp_id], 'kapb'


    elif re.search('KP\\d+A', cp_id) is not None:
        s['list'], swithc = getkplx(), getkplx(2)
        s['dir'], s['abs'] = swithc[cp_id], 'pklx'
    elif re.search('ZP\\d+A', cp_id) is not None:
        s['list'], swithc = getzplx(), getzplx(2)
        s['dir'], s['abs'] = swithc[cp_id], 'zplx'
    elif re.search('KS\\d+A', cp_id) is not None:
        s['list'], swithc = getkslx(), getkslx(2)
        s['dir'], s['abs'] = swithc[cp_id], 'kslx'
    elif re.search('ZK\\d+A', cp_id) is not None:
        s['list'], swithc = getzklx(), getzklx(2)
        s['dir'], s['abs'] = swithc[cp_id], 'zklx'

    # 整流桥
    elif 'SQL' in cp_id:
        s['list'], swithc = getsql(), getsql(2)
        s['dir'], s['abs'] = swithc[cp_id], 'sql'


    elif 'QL' in cp_id:
        s['list'], swithc = getql(), getql(2)
        s['dir'], s['abs'] = swithc[cp_id], 'ql'
    elif 'MDST' in cp_id:
        s['list'], swithc = getmdst(), getmdst(2)
        s['dir'], s['abs'] = swithc[cp_id], 'mdst'
    elif 'MDQ' in cp_id:
        s['list'], swithc = getmdq(), getmdq(2)
        s['dir'], s['abs'] = swithc[cp_id], 'mdq'
    elif 'MDS' in cp_id:
        s['list'], swithc = getmds(), getmds(2)
        s['dir'], s['abs'] = swithc[cp_id], 'mds'
    elif 'MFQ' in cp_id:
        s['list'], swithc = getmfq(), getmfq(2)
        s['dir'], s['abs'] = swithc[cp_id], 'mfq'
    elif '4ZQ' in cp_id:
        s['list'], swithc = getfzq(), getfzq(2)
        s['dir'], s['abs'] = swithc[cp_id], '4zq'
    elif 'KBPC' in cp_id:
        s['list'], swithc = getkbpc(), getkbpc(2)
        s['dir'], s['abs'] = swithc[cp_id], 'kbpc'
    # 散热器
    elif 'SF' in cp_id:
        s['list'], swithc = getsf(), getsf(2)
        s['dir'], s['abs'] = swithc[cp_id], 'sf'
    elif 'SS' in cp_id:
        s['list'], swithc = getss(), getss(2)
        s['dir'], s['abs'] = swithc[cp_id], 'ss'
    elif 'SL' in cp_id:
        s['list'], swithc = getlxsr(), getlxsr(2)
        s['dir'], s['abs'] = swithc[cp_id], 'lxsr'
    elif '风机' in cp_id:
        s['list'], swithc = getfj(), getfj(2)
        s['dir'], s['abs'] = swithc[cp_id], 'fj'
    elif '触发器' in cp_id:
        s['list'], swithc = getcfq(), getcfq(2)
        s['dir'], s['abs'] = swithc[cp_id], 'cfq'
    elif 'ZF' in cp_id or 'H' in cp_id:
        s['list'], swithc = getgyjgtjdq(), getgyjgtjdq(2)
        s['dir'], s['abs'] = swithc[cp_id], 'gyjgtjdq'

    return render(request, "cpxq.html", s)


# 模块系列
def czsearch(request):
    name = request.GET.get('text').upper()
    s = {'name': '', 'ky': name, 'dir': ''}
    # 判断型号
    if 'MTC' in name:
        s['name'] = zip(['mtc'], [getmtclist()])
    elif 'MD' == name or re.search('MD\\d+', name) is not None:
        s['name'] = zip(['md'], [getmdlist()])
    elif 'MDC' in name:
        s['name'] = zip(['mdc'], [getmdclist()])
    elif 'MDA' in name:
        s['name'] = zip(['mda'], [getmdalist()])
    elif 'MDK' in name:
        s['name'] = zip(['mdk'], [getmdklist()])
    elif 'MTX' in name:
        s['name'] = zip(['mtx'], [getmtxlist()])
    elif 'MTA' in name:
        s['name'] = zip(['mta'], [getmtalist()])
    elif 'MTK' in name:
        s['name'] = zip(['mtk'], [getmtklist()])
    elif 'MFA' in name:
        s['name'] = zip(['mfa'], [getmfalist()])
    elif 'MFC' in name:
        s['name'] = zip(['mfc'], [getmfclist()])
    # 固态继电器
    elif re.search('SSR\\d+DA', name) is not None:
        s['name'] = zip(['ssrad'], [getssrda()])
    elif re.search('SSR\\d+AA', name) is not None:
        s['name'] = zip(['ssraa'], [getssraa()])
    elif re.search('SSR\\d+VA', name) is not None:
        s['name'] = zip(['ssrva'], [getssrva()])
    elif re.search('SSR\\d+DD', name) is not None:
        s['name'] = zip(['ssrdd'], [getssrdd()])
    elif re.search('JGX-3 \\d+DA', name) is not None or re.search('JGX-3\\d+DA', name) is not None:
        s['name'] = zip(['jgxda'], [getjgxda()])
    elif re.search('JGX-3 \\d+AA', name) is not None or re.search('JGX-3\\d+AA', name) is not None:
        s['name'] = zip(['jgxaa'], [getjgxaa()])
    # 螺旋系列 dan 平板
    elif 'KP' in name:
        s['name'] = zip(['kplx', 'kppb'], [getkplx(), getkppb()])
    elif 'ZP' in name:
        s['name'] = zip(['zplx', 'zppb'], [getzplx(), getzppb()])
    elif 'KS' in name:
        s['name'] = zip(['kslx', 'kspb'], [getkslx(), getkspb()])
    elif 'ZK' in name:
        s['name'] = zip(['zklx', 'zkpb'], [getzklx(), getzkpb()])
    elif 'KK' in name:
        s['name'] = zip(['kkpb'], [getkkpb()])
    elif 'KA' in name:
        s['name'] = zip(['kapb'], [getkapb()])
    # 整流桥
    elif 'SQL' in name:
        s['name'] = zip(['sql'], [getsql()])
    elif 'MDST' in name:
        s['name'] = zip(['mdst'], [getmdst()])
    elif 'MDS' in name:
        s['name'] = zip(['mds'], [getmds()])
    elif 'QL' in name:
        s['name'] = zip(['ql'], [getql()])
    elif 'MDQ' in name:
        s['name'] = zip(['mdq'], [getmdq()])
    elif 'MFQ' in name:
        s['name'] = zip(['mfq'], [getmfq()])
    elif '4ZQ' in name:
        s['name'] = zip(['4zq'], [getfzq()])
    elif 'KBPC' in name:
        s['name'] = zip(['kbpc'], [getkbpc()])
    elif 'SF' in name:
        s['name'] = zip(['sf'], [getsf()])
    elif 'SS' in name:
        s['name'] = zip(['ss'], [getss()])
    elif 'SL' in name:
        s['name'] = zip(['lxsr'], [getlxsr()])
    elif '风机' in name:
        s['name'] = zip(['fj'], [getfj()])
    elif '触发器' in name:
        s['name'] = zip(['cfq'], [getcfq()])
    elif 'H' in name or 'ZF' in name:
        s['name'] = zip(['gyjgtjdq'], [getgyjgtjdq()])

    else:
        s['node'] = '1'
    # ky 搜索关键字
    return render(request, "czsearch.html", s)


def getmtclist(munber=1):
    if munber == 1:
        return [{'name': 'MTC25A', 'img': '25'},
                {'name': 'MTC55A', 'img': '55'},
                {'name': 'MTC70A', 'img': '70'},
                {'name': 'MTC90A', 'img': '90'},
                {'name': 'MTC110A', 'img': '110'},
                {'name': 'MTC135A', 'img': '135'},
                {'name': 'MTC160A', 'img': '160'},
                {'name': 'MTC200A', 'img': '200'},
                {'name': 'MTC200A扁型', 'img': '200b'},
                {'name': 'MTC200A大型', 'img': '200d'},
                {'name': 'MTC250A', 'img': '250'},
                {'name': 'MTC300A', 'img': '300'},
                {'name': 'MTC300A水冷', 'img': '300l'},
                {'name': 'MTC400A', 'img': '400'},
                {'name': 'MTC400A大型', 'img': '400d'},
                {'name': 'MTC500A', 'img': '500'},
                {'name': 'MTC500A水冷', 'img': '500l'},
                {'name': 'MTC600A', 'img': '600'},
                {'name': 'MTC800A', 'img': '800'},
                {'name': 'MTC800A水冷', 'img': '800l'},
                {'name': 'MTC800A大型', 'img': '800d'},
                {'name': 'MTC1000A', 'img': '1000'},
                {'name': 'MTC1000A水冷', 'img': '1000l'}]
    else:
        return {'MTC25A': '25', 'MTC55A': '55', 'MTC70A': '70', 'MTC90A': '90', 'MTC110A': '110',
                'MTC135A': '135', 'MTC160A': '160', 'MTC200A': '200', 'MTC200A扁型': '200b', 'MTC200A大型': '200d',
                'MTC250A': '250', 'MTC300A': '300', 'MTC300A水冷': '300l', 'MTC400A': '400', 'MTC400A大型': '400d',
                'MTC500A': '500',
                'MTC500A水冷': '500l', 'MTC600A': '600', 'MTC800A': '800', 'MTC800A水冷': '800l', 'MTC800A大型': '800d',
                'MTC1000A': '1000', 'MTC1000A水冷': '1000l'}


def getmdclist(munber=1):
    if munber == 1:
        return [{'name': 'MDC25A', 'img': '25'},
                {'name': 'MDC55A', 'img': '55'},
                {'name': 'MDC70A', 'img': '70'},
                {'name': 'MDC90A', 'img': '90'},
                {'name': 'MDC110A', 'img': '110'},
                {'name': 'MDC135A', 'img': '135'},
                {'name': 'MDC160A', 'img': '160'},
                {'name': 'MDC200A', 'img': '200'},
                {'name': 'MDC200A扁型', 'img': '200b'},
                {'name': 'MDC200A大型', 'img': '200d'},
                {'name': 'MDC250A', 'img': '250'},
                {'name': 'MDC300A', 'img': '300'},
                {'name': 'MDC400A', 'img': '400'},
                {'name': 'MDC400A大型', 'img': '400d'},
                {'name': 'MDC500A', 'img': '500'},
                {'name': 'MDC600A', 'img': '600'},
                {'name': 'MDC800A', 'img': '800'},
                {'name': 'MDC800A大型', 'img': '800d'},
                {'name': 'MDC1000A', 'img': '1000'}]
    else:
        return {'MDC25A': '25', 'MDC55A': '55', 'MDC70A': '70', 'MDC90A': '90', 'MDC110A': '110',
                'MDC135A': '135', 'MDC160A': '160', 'MDC200A': '200', 'MDC200A扁型': '200b', 'MDC200A大型': '200d',
                'MDC250A': '250', 'MDC300A': '300', 'MDC400A': '400', 'MDC400A大型': '400d',
                'MDC500A': '500',
                'MDC600A': '600', 'MDC800A': '800', 'MDC800A大型': '800d',
                'MDC1000A': '1000'}


def getmdalist(munber=1):
    if munber == 1:
        return [{'name': 'MDA25A', 'img': '25'},
                {'name': 'MDA55A', 'img': '55'},
                {'name': 'MDA70A', 'img': '70'},
                {'name': 'MDA90A', 'img': '90'},
                {'name': 'MDA110A', 'img': '110'},
                {'name': 'MDA135A', 'img': '135'},
                {'name': 'MDA160A', 'img': '160'},
                {'name': 'MDA200A', 'img': '200'},
                {'name': 'MDA200A扁型', 'img': '200b'},
                {'name': 'MDA200A大型', 'img': '200d'},
                {'name': 'MDA250A', 'img': '250'},
                {'name': 'MDA300A', 'img': '300'},
                {'name': 'MDA400A', 'img': '400'},
                {'name': 'MDA400A大型', 'img': '400d'},
                {'name': 'MDA500A', 'img': '500'},
                {'name': 'MDA600A', 'img': '600'},
                {'name': 'MDA800A', 'img': '800'},
                {'name': 'MDA800A大型', 'img': '800d'},
                {'name': 'MDA1000A', 'img': '1000'}]
    else:
        return {'MDA25A': '25', 'MDA55A': '55', 'MDA70A': '70', 'MDA90A': '90', 'MDA110A': '110',
                'MDA135A': '135', 'MDA160A': '160', 'MDA200A': '200', 'MDA200A扁型': '200b', 'MDA200A大型': '200d',
                'MDA250A': '250', 'MDA300A': '300', 'MDA400A': '400', 'MDA400A大型': '400d',
                'MDA500A': '500',
                'MDA600A': '600', 'MDA800A': '800', 'MDA800A大型': '800d',
                'MDA1000A': '1000'}


def getmdklist(munber=1):
    if munber == 1:
        return [{'name': 'MDK25A', 'img': '25'},
                {'name': 'MDK55A', 'img': '55'},
                {'name': 'MDK70A', 'img': '70'},
                {'name': 'MDK90A', 'img': '90'},
                {'name': 'MDK110A', 'img': '110'},
                {'name': 'MDK135A', 'img': '135'},
                {'name': 'MDK160A', 'img': '160'},
                {'name': 'MDK200A', 'img': '200'},
                {'name': 'MDK200A扁型', 'img': '200b'},
                {'name': 'MDK200A大型', 'img': '200d'},
                {'name': 'MDK250A', 'img': '250'},
                {'name': 'MDK300A', 'img': '300'},
                {'name': 'MDK400A', 'img': '400'},
                {'name': 'MDK400A大型', 'img': '400d'},
                {'name': 'MDK500A', 'img': '500'},
                {'name': 'MDK600A', 'img': '600'},
                {'name': 'MDK800A', 'img': '800'},
                {'name': 'MDK800A大型', 'img': '800d'},
                {'name': 'MDK1000A', 'img': '1000'}]
    else:
        return {'MDK25A': '25', 'MDK55A': '55', 'MDK70A': '70', 'MDK90A': '90', 'MDK110A': '110',
                'MDK135A': '135', 'MDK160A': '160', 'MDK200A': '200', 'MDK200A扁型': '200b', 'MDK200A大型': '200d',
                'MDK250A': '250', 'MDK300A': '300', 'MDK400A': '400', 'MDK400A大型': '400d',
                'MDK500A': '500',
                'MDK600A': '600', 'MDK800A': '800', 'MDK800A大型': '800d',
                'MDK1000A': '1000'}


def getmtalist(munber=1):
    if munber == 1:
        return [{'name': 'MTA25A', 'img': '25'},
                {'name': 'MTA55A', 'img': '55'},
                {'name': 'MTA70A', 'img': '70'},
                {'name': 'MTA90A', 'img': '90'},
                {'name': 'MTA110A', 'img': '110'},
                {'name': 'MTA135A', 'img': '135'},
                {'name': 'MTA160A', 'img': '160'},
                {'name': 'MTA200A', 'img': '200'},
                {'name': 'MTA200A扁型', 'img': '200b'},
                {'name': 'MTA200A大型', 'img': '200d'},
                {'name': 'MTA250A', 'img': '250'},
                {'name': 'MTA300A', 'img': '300'},
                {'name': 'MTA400A', 'img': '400'},
                {'name': 'MTA400A大型', 'img': '400d'},
                {'name': 'MTA500A', 'img': '500'},
                {'name': 'MTA600A', 'img': '600'},
                {'name': 'MTA800A', 'img': '800'},
                {'name': 'MTA800A大型', 'img': '800d'},
                {'name': 'MTA1000A', 'img': '1000'}]
    else:
        return {'MTA25A': '25', 'MTA55A': '55', 'MTA70A': '70', 'MTA90A': '90', 'MTA110A': '110',
                'MTA135A': '135', 'MTA160A': '160', 'MTA200A': '200', 'MTA200A扁型': '200b', 'MTA200A大型': '200d',
                'MTA250A': '250', 'MTA300A': '300', 'MTA400A': '400', 'MTA400A大型': '400d',
                'MTA500A': '500',
                'MTA600A': '600', 'MTA800A': '800', 'MTA800A大型': '800d',
                'MTA1000A': '1000'}


def getmtxlist(munber=1):
    if munber == 1:
        return [{'name': 'MTX25A', 'img': '25'},
                {'name': 'MTX55A', 'img': '55'},
                {'name': 'MTX70A', 'img': '70'},
                {'name': 'MTX90A', 'img': '90'},
                {'name': 'MTX110A', 'img': '110'},
                {'name': 'MTX135A', 'img': '135'},
                {'name': 'MTX160A', 'img': '160'},
                {'name': 'MTX200A', 'img': '200'},
                {'name': 'MTX200A扁型', 'img': '200b'},
                {'name': 'MTX200A大型', 'img': '200d'},
                {'name': 'MTX250A', 'img': '250'},
                {'name': 'MTX300A', 'img': '300'},
                {'name': 'MTX400A', 'img': '400'},
                {'name': 'MTX400A大型', 'img': '400d'},
                {'name': 'MTX500A', 'img': '500'},
                {'name': 'MTX600A', 'img': '600'},
                {'name': 'MTX800A', 'img': '800'},
                {'name': 'MTX800A大型', 'img': '800d'},
                {'name': 'MTX1000A', 'img': '1000'}]
    else:
        return {'MTX25A': '25', 'MTX55A': '55', 'MTX70A': '70', 'MTX90A': '90', 'MTX110A': '110',
                'MTX135A': '135', 'MTX160A': '160', 'MTX200A': '200', 'MTX200A扁型': '200b', 'MTX200A大型': '200d',
                'MTX250A': '250', 'MTX300A': '300', 'MTX400A': '400', 'MTX400A大型': '400d',
                'MTX500A': '500',
                'MTX600A': '600', 'MTX800A': '800', 'MTX800A大型': '800d',
                'MTX1000A': '1000'}


def getmtklist(munber=1):
    if munber == 1:
        return [{'name': 'MTK25A', 'img': '25'},
                {'name': 'MTK55A', 'img': '55'},
                {'name': 'MTK70A', 'img': '70'},
                {'name': 'MTK90A', 'img': '90'},
                {'name': 'MTK110A', 'img': '110'},
                {'name': 'MTK135A', 'img': '135'},
                {'name': 'MTK160A', 'img': '160'},
                {'name': 'MTK200A', 'img': '200'},
                {'name': 'MTK200A扁型', 'img': '200b'},
                {'name': 'MTK200A大型', 'img': '200d'},
                {'name': 'MTK250A', 'img': '250'},
                {'name': 'MTK300A', 'img': '300'},
                {'name': 'MTK400A', 'img': '400'},
                {'name': 'MTK400A大型', 'img': '400d'},
                {'name': 'MTK500A', 'img': '500'},
                {'name': 'MTK600A', 'img': '600'},
                {'name': 'MTK800A', 'img': '800'},
                {'name': 'MTK800A大型', 'img': '800d'},
                {'name': 'MTK1000A', 'img': '1000'}]
    else:
        return {'MTK25A': '25', 'MTK55A': '55', 'MTK70A': '70', 'MTK90A': '90', 'MTK110A': '110',
                'MTK135A': '135', 'MTK160A': '160', 'MTK200A': '200', 'MTK200A扁型': '200b', 'MTK200A大型': '200d',
                'MTK250A': '250', 'MTK300A': '300', 'MTK400A': '400', 'MTK400A大型': '400d',
                'MTK500A': '500',
                'MTK600A': '600', 'MTK800A': '800', 'MTK800A大型': '800d',
                'MTK1000A': '1000'}


def getmdlist(munber=1):
    if munber == 1:
        return [{'name': 'MD25A', 'img': '25'},
                {'name': 'MD55A', 'img': '55'},
                {'name': 'MD70A', 'img': '70'},
                {'name': 'MD90A', 'img': '90'},
                {'name': 'MD110A', 'img': '110'},
                {'name': 'MD135A', 'img': '135'},
                {'name': 'MD160A', 'img': '160'},
                {'name': 'MD200A', 'img': '200'},
                {'name': 'MD200A扁型', 'img': '200b'},
                {'name': 'MD200A大型', 'img': '200d'},
                {'name': 'MD250A', 'img': '250'},
                {'name': 'MD300A', 'img': '300'},
                {'name': 'MD400A', 'img': '400'},
                {'name': 'MD400A大型', 'img': '400d'},
                {'name': 'MD500A', 'img': '500'},
                {'name': 'MD600A', 'img': '600'},
                {'name': 'MD800A', 'img': '800'},
                {'name': 'MD800A大型', 'img': '800d'},
                {'name': 'MD1000A', 'img': '1000'}]
    else:
        return {'MD25A': '25', 'MD55A': '55', 'MD70A': '70', 'MD90A': '90', 'MD110A': '110',
                'MD135A': '135', 'MD160A': '160', 'MD200A': '200', 'MD200A扁型': '200b', 'MD200A大型': '200d',
                'MD250A': '250', 'MD300A': '300', 'MD400A': '400', 'MD400A大型': '400d',
                'MD500A': '500',
                'MD600A': '600', 'MD800A': '800', 'MD800A大型': '800d',
                'MD1000A': '1000'}


def getmfclist(munber=1):
    if munber == 1:
        return [{'name': 'MFC25A', 'img': '25'},
                {'name': 'MFC55A', 'img': '55'},
                {'name': 'MFC70A', 'img': '70'},
                {'name': 'MFC90A', 'img': '90'},
                {'name': 'MFC110A', 'img': '110'},
                {'name': 'MFC135A', 'img': '135'},
                {'name': 'MFC160A', 'img': '160'},
                {'name': 'MFC200A', 'img': '200'},
                {'name': 'MFC200A扁型', 'img': '200b'},
                {'name': 'MFC200A大型', 'img': '200d'},
                {'name': 'MFC250A', 'img': '250'},
                {'name': 'MFC300A', 'img': '300'},
                {'name': 'MFC300A水冷', 'img': '300l'},
                {'name': 'MFC400A', 'img': '400'},
                {'name': 'MFC400A大型', 'img': '400d'},
                {'name': 'MFC500A', 'img': '500'},
                {'name': 'MFC500A水冷', 'img': '500l'},
                {'name': 'MFC600A', 'img': '600'},
                {'name': 'MFC800A', 'img': '800'},
                {'name': 'MFC800A水冷', 'img': '800l'},
                {'name': 'MFC800A大型', 'img': '800d'},
                {'name': 'MFC1000A', 'img': '1000'},
                {'name': 'MFC1000A水冷', 'img': '1000l'}]
    else:
        return {'MFC25A': '25', 'MFC55A': '55', 'MFC70A': '70', 'MFC90A': '90', 'MFC110A': '110',
                'MFC135A': '135', 'MFC160A': '160', 'MFC200A': '200', 'MFC200A扁型': '200b', 'MFC200A大型': '200d',
                'MFC250A': '250', 'MFC300A': '300', 'MFC300A水冷': '300l', 'MFC400A': '400', 'MFC400A大型': '400d',
                'MFC500A': '500',
                'MFC500A水冷': '500l', 'MFC600A': '600', 'MFC800A': '800', 'MFC800A水冷': '800l', 'MFC800A大型': '800d',
                'MFC1000A': '1000', 'MFC1000A水冷': '1000l'}


def getmfalist(munber=1):
    if munber == 1:
        return [{'name': 'MFA25A', 'img': '25'},
                {'name': 'MFA55A', 'img': '55'},
                {'name': 'MFA70A', 'img': '70'},
                {'name': 'MFA90A', 'img': '90'},
                {'name': 'MFA110A', 'img': '110'},
                {'name': 'MFA135A', 'img': '135'},
                {'name': 'MFA160A', 'img': '160'},
                {'name': 'MFA200A', 'img': '200'},
                {'name': 'MFA200A扁型', 'img': '200b'},
                {'name': 'MFA200A大型', 'img': '200d'},
                {'name': 'MFA250A', 'img': '250'},
                {'name': 'MFA300A', 'img': '300'},
                {'name': 'MFA400A', 'img': '400'},
                {'name': 'MFA400A大型', 'img': '400d'},
                {'name': 'MFA500A', 'img': '500'},
                {'name': 'MFA600A', 'img': '600'},
                {'name': 'MFA800A', 'img': '800'},
                {'name': 'MFA800A大型', 'img': '800d'},
                {'name': 'MFA1000A', 'img': '1000'}]
    else:
        return {'MFA25A': '25', 'MFA55A': '55', 'MFA70A': '70', 'MFA90A': '90', 'MFA110A': '110',
                'MFA135A': '135', 'MFA160A': '160', 'MFA200A': '200', 'MFA200A扁型': '200b', 'MFA200A大型': '200d',
                'MFA250A': '250', 'MFA300A': '300', 'MFA400A': '400', 'MFA400A大型': '400d',
                'MFA500A': '500',
                'MFA600A': '600', 'MFA800A': '800', 'MFA800A大型': '800d',
                'MFA1000A': '1000'}


# 固态系列
def getssraa(munber=1):
    if munber == 1:
        return [{'name': 'SSR10AA', 'img': '10'},
                {'name': 'SSR15AA', 'img': '15'},
                {'name': 'SSR20AA', 'img': '20'},
                {'name': 'SSR25AA', 'img': '25'},
                {'name': 'SSR30AA', 'img': '30'},
                {'name': 'SSR40AA', 'img': '40'},
                {'name': 'SSR50AA', 'img': '50'},
                {'name': 'SSR60AA', 'img': '60'},
                {'name': 'SSR80AA', 'img': '80'},
                {'name': 'SSR100AA', 'img': '100'}]

    else:
        return {'SSR10AA': '10', 'SSR15AA': '15', 'SSR20AA': '20', 'SSR25AA': '25', 'SSR30AA': '30',
                'SSR40AA': '40', 'SSR50AA': '50', 'SSR60AA': '60', 'SSR80AA': '80', 'SSR100AA': '100'}


def getssrva(munber=1):
    if munber == 1:
        return [{'name': 'SSR10VA', 'img': '10'},
                {'name': 'SSR15VA', 'img': '15'},
                {'name': 'SSR20VA', 'img': '20'},
                {'name': 'SSR25VA', 'img': '25'},
                {'name': 'SSR30VA', 'img': '30'},
                {'name': 'SSR40VA', 'img': '40'},
                {'name': 'SSR50VA', 'img': '50'},
                {'name': 'SSR60VA', 'img': '60'},
                {'name': 'SSR80VA', 'img': '80'},
                {'name': 'SSR100VA', 'img': '100'}]

    else:
        return {'SSR10VA': '10', 'SSR15VA': '15', 'SSR20VA': '20', 'SSR25VA': '25', 'SSR30VA': '30',
                'SSR40VA': '40', 'SSR50VA': '50', 'SSR60VA': '60', 'SSR80VA': '80', 'SSR100VA': '100'}


def getssrda(munber=1):
    if munber == 1:
        return [{'name': 'SSR10DA', 'img': '10'},
                {'name': 'SSR15DA', 'img': '15'},
                {'name': 'SSR20DA', 'img': '20'},
                {'name': 'SSR25DA', 'img': '25'},
                {'name': 'SSR30DA', 'img': '30'},
                {'name': 'SSR40DA', 'img': '40'},
                {'name': 'SSR50DA', 'img': '50'},
                {'name': 'SSR60DA', 'img': '60'},
                {'name': 'SSR80DA', 'img': '80'},
                {'name': 'SSR100DA', 'img': '100'},
                {'name': 'SSR120DA', 'img': '120'},
                {'name': 'SSR150DA', 'img': '150'}]

    else:
        return {'SSR10DA': '10', 'SSR15DA': '15', 'SSR20DA': '20', 'SSR25DA': '25', 'SSR30DA': '30',
                'SSR40DA': '40', 'SSR50DA': '50', 'SSR60DA': '60', 'SSR80DA': '80', 'SSR100DA': '100',
                'SSR120DA': '100', 'SSR150DA': '150'}


def getssrdd(munber=1):
    if munber == 1:
        return [{'name': 'SSR10DD', 'img': '10'},
                {'name': 'SSR15DD', 'img': '15'},
                {'name': 'SSR20DD', 'img': '20'},
                {'name': 'SSR25DD', 'img': '25'},
                {'name': 'SSR30DD', 'img': '30'},
                {'name': 'SSR40DD', 'img': '40'},
                {'name': 'SSR50DD', 'img': '50'},
                {'name': 'SSR60DD', 'img': '60'},
                {'name': 'SSR80DD', 'img': '80'},
                {'name': 'SSR100DD', 'img': '100'},
                {'name': 'SSR120DD', 'img': '120'},
                {'name': 'SSR150DD', 'img': '150'}]

    else:
        return {'SSR10DD': '10', 'SSR15DD': '15', 'SSR20DD': '20', 'SSR25DD': '25', 'SSR30DD': '30',
                'SSR40DD': '40', 'SSR50DD': '50', 'SSR60DD': '60', 'SSR80DD': '80', 'SSR100DD': '100',
                'SSR120DD': '100', 'SSR150DD': '150'}


def getjgxaa(munber=1):
    if munber == 1:
        return [{'name': 'JGX-3 10AA', 'img': '10'},
                {'name': 'JGX-3 15AA', 'img': '15'},
                {'name': 'JGX-3 20AA', 'img': '20'},
                {'name': 'JGX-3 25AA', 'img': '25'},
                {'name': 'JGX-3 40AA', 'img': '40'},
                {'name': 'JGX-3 50AA', 'img': '50'},
                {'name': 'JGX-3 60AA', 'img': '60'},
                {'name': 'JGX-3 80AA', 'img': '80'},
                {'name': 'JGX-3 100AA', 'img': '100'},
                {'name': 'JGX-3 120AA', 'img': '120'},
                {'name': 'JGX-3 150AA', 'img': '150'},
                {'name': 'JGX-3 200AA', 'img': '200'}]

    else:
        return {'JGX-3 10AA': '10', 'JGX-3 15AA': '15', 'JGX-3 20AA': '20', 'JGX-3 25AA': '25',
                'JGX-3 40AA': '40', 'JGX-3 50AA': '50', 'JGX-3 60AA': '60', 'JGX-3 80AA': '80', 'JGX-3 100AA': '100',
                'JGX-3 120AA': '100', 'JGX-3 150AA': '150', 'JGX-3 200AA': '200'}


def getjgxda(munber=1):
    if munber == 1:
        return [{'name': 'JGX-3 10DA', 'img': '10'},
                {'name': 'JGX-3 15DA', 'img': '15'},
                {'name': 'JGX-3 20DA', 'img': '20'},
                {'name': 'JGX-3 25DA', 'img': '25'},
                {'name': 'JGX-3 40DA', 'img': '40'},
                {'name': 'JGX-3 50DA', 'img': '50'},
                {'name': 'JGX-3 60DA', 'img': '60'},
                {'name': 'JGX-3 80DA', 'img': '80'},
                {'name': 'JGX-3 100DA', 'img': '100'},
                {'name': 'JGX-3 120DA', 'img': '120'},
                {'name': 'JGX-3 150DA', 'img': '150'},
                {'name': 'JGX-3 200DA', 'img': '200'}]

    else:
        return {'JGX-3 10DA': '10', 'JGX-3 15DA': '15', 'JGX-3 20DA': '20', 'JGX-3 25DA': '25',
                'JGX-3 40DA': '40', 'JGX-3 50DA': '50', 'JGX-3 60DA': '60', 'JGX-3 80DA': '80', 'JGX-3 100DA': '100',
                'JGX-3 120DA': '100', 'JGX-3 150DA': '150', 'JGX-3 200DA': '200'}


# 螺旋系列 KP螺旋 ZP 螺旋 KS 螺旋 ZK  螺旋

def getzplx(munber=1):
    if munber == 1:
        return [{'name': 'ZP1A', 'img': '1'},
                {'name': 'ZP5A', 'img': '5'},
                {'name': 'ZP10A', 'img': '10'},
                {'name': 'ZP20A', 'img': '20'},
                {'name': 'ZP20A带线', 'img': '20x'},
                {'name': 'ZP30A', 'img': '30'},
                {'name': 'ZP50A', 'img': '50'},
                {'name': 'ZP50A反向', 'img': '50f'},
                {'name': 'ZP100A', 'img': '100'},
                {'name': 'ZP100A反向', 'img': '100f'},
                {'name': 'ZP200A', 'img': '200'},
                {'name': 'ZP200A反向', 'img': '200f'},
                {'name': 'ZP300A', 'img': '300'},
                {'name': 'ZP300A反向', 'img': '300f'},
                {'name': 'ZP400A', 'img': '400'},
                {'name': 'ZP500A', 'img': '500'}]

    else:
        return {'ZP1A': '1', 'ZP5A': '5', 'ZP10A': '10', 'ZP20A': '20',
                'ZP20A带线': '20x', 'ZP30A': '30', 'ZP50A': '50', 'ZP50A反向': '50f', 'ZP100A': '100', 'ZP100A反向': '100f',
                'ZP200A': '200', 'ZP200A反向': '200f',
                'ZP300A': '300', 'ZP300A反向': '300f', 'ZP400A': '400', 'ZP500A': '500'}


def getkplx(munber=1):
    if munber == 1:
        return [{'name': 'KP1A', 'img': '1'},
                {'name': 'KP5A', 'img': '5'},
                {'name': 'KP10A', 'img': '10'},
                {'name': 'KP20A', 'img': '20'},
                {'name': 'KP20A带线', 'img': '20x'},
                {'name': 'KP30A', 'img': '30'},
                {'name': 'KP50A', 'img': '50'},
                {'name': 'KP100A', 'img': '100'},
                {'name': 'KP200A', 'img': '200'},
                {'name': 'KP300A', 'img': '300'},
                {'name': 'KP400A', 'img': '400'},
                {'name': 'KP500A', 'img': '500'}]

    else:
        return {'KP1A': '1', 'KP5A': '5', 'KP10A': '10', 'KP20A': '20',
                'KP20A带线': '20x', 'KP30A': '30', 'KP50A': '50', 'KP100A': '100', 'KP200A': '200',
                'KP300A': '300', 'KP400A': '400', 'KP500A': '500'}


def getkslx(munber=1):
    if munber == 1:
        return [{'name': 'KS1A', 'img': '1'},
                {'name': 'KS5A', 'img': '5'},
                {'name': 'KS10A', 'img': '10'},
                {'name': 'KS20A', 'img': '20'},
                {'name': 'KS30A', 'img': '30'},
                {'name': 'KS50A', 'img': '50'},
                {'name': 'KS100A', 'img': '100'},
                {'name': 'KS200A', 'img': '200'},
                {'name': 'KS300A', 'img': '300'}]

    else:
        return {'KS1A': '1', 'KS5A': '5', 'KS10A': '10', 'KS20A': '20',
                'KS30A': '30', 'KS50A': '50', 'KS100A': '100', 'KS200A': '200',
                'KS300A': '300'}


def getzklx(munber=1):
    if munber == 1:
        return [{'name': 'ZK25A', 'img': '25'},
                {'name': 'ZK40A', 'img': '40'},
                {'name': 'ZK70A', 'img': '70'},
                {'name': 'ZK200A', 'img': '200'},
                {'name': 'ZK200A反向', 'img': '200f'},
                {'name': 'ZK300A', 'img': '300'},
                {'name': 'ZK300A反向', 'img': '300f'}]

    else:
        return {'ZK25A': '25', 'ZK40A': '40', 'ZK70A': '70', 'ZK200A': '200',
                'ZK200A反向': '200f', 'ZK300A': '300', 'ZK300A反向': '300f'}


# 平板系列 kp zp ks  kk zk KA

def getkppb(munber=1):
    if munber == 1:
        return [{'name': 'KP200A(凹型)', 'img': '200o'},
                {'name': 'KP300A(凹型)', 'img': '300o'},
                {'name': 'KP500A(凹型)', 'img': '500o'},
                {'name': 'KP800A(凹型)', 'img': '800o'},
                {'name': 'KP1000A(凹型)', 'img': '1000o'},

                {'name': 'KP200A(半凸)', 'img': '200b'},
                {'name': 'KP300A(半凸)', 'img': '300b'},
                {'name': 'KP500A(半凸)', 'img': '500b'},
                {'name': 'KP800A(半凸)', 'img': '800b'},
                {'name': 'KP1000A(半凸)', 'img': '1000b'},

                {'name': 'KP200A(凸型)', 'img': '200t'},
                {'name': 'KP300A(凸型)', 'img': '300t'},
                {'name': 'KP400A(凸型)', 'img': '400t'},
                {'name': 'KP500A(凸型)', 'img': '500t'},
                {'name': 'KP600A(凸型)', 'img': '600t'},
                {'name': 'KP800A(凸型)', 'img': '800t'},
                {'name': 'KP1000A(凸型)', 'img': '1000t'},
                {'name': 'KP1200A(凸型)', 'img': '1200t'},
                {'name': 'KP1500A(凸型)', 'img': '1500t'},
                {'name': 'KP1600A(凸型)', 'img': '1600t'},
                {'name': 'KP2000A(凸型)', 'img': '2000t'},
                {'name': 'KP2500A(凸型)', 'img': '2500t'},
                {'name': 'KP3000A(凸型)', 'img': '3000t'},
                {'name': 'KP4000A(凸型)', 'img': '4000t'},
                {'name': 'KP5000A(凸型)', 'img': '5000t'},
                {'name': 'KP6000A(凸型)', 'img': '6000t'},
                {'name': 'KP7000A(凸型)', 'img': '7000t'}]

    else:
        return {'KP200A(凹型)': '200o', 'KP300A(凹型)': '300o', 'KP500A(凹型)': '500o', 'KP800A(凹型)': '800o',
                'KP1000A(凹型)': '1000o',

                'KP200A(半凸)': '200b', 'KP300A(半凸)': '300b', 'KP500A(半凸)': '500b', 'KP800A(半凸)': '800b',
                'KP1000A(半凸)': '1000b',

                'KP200A(凸型)': '200t', 'KP300A(凸型)': '300t', 'KP400A(凸型)': '400t', 'KP500A(凸型)': '500t',
                'KP600A(凸型)': '600t', 'KP800A(凸型)': '800t',
                'KP1000A(凸型)': '1000t', 'KP1200A(凸型)': '1200t', 'KP1500A(凸型)': '1500t', 'KP2000A(凸型)': '2000t',
                'KP2500A(凸型)': '2500t', 'KP3000A(凸型)': '3000t',
                'KP4000A(凸型)': '4000t', 'KP5000A(凸型)': '5000t', 'KP6000A(凸型)': '6000t', 'KP7000A(凸型)': '7000t'}


def getzppb(munber=1):
    if munber == 1:
        return [{'name': 'ZP200A(凹型)', 'img': '200o'},
                {'name': 'ZP300A(凹型)', 'img': '300o'},
                {'name': 'ZP500A(凹型)', 'img': '500o'},
                {'name': 'ZP800A(凹型)', 'img': '800o'},
                {'name': 'ZP1000A(凹型)', 'img': '1000o'},

                {'name': 'ZP200A(半凸)', 'img': '200b'},
                {'name': 'ZP300A(半凸)', 'img': '300b'},
                {'name': 'ZP500A(半凸)', 'img': '500b'},
                {'name': 'ZP800A(半凸)', 'img': '800b'},
                {'name': 'ZP1000A(半凸)', 'img': '1000b'},

                {'name': 'ZP200A(凸型)', 'img': '200t'},
                {'name': 'ZP300A(凸型)', 'img': '300t'},
                {'name': 'ZP400A(凸型)', 'img': '400t'},
                {'name': 'ZP500A(凸型)', 'img': '500t'},
                {'name': 'ZP600A(凸型)', 'img': '600t'},
                {'name': 'ZP800A(凸型)', 'img': '800t'},
                {'name': 'ZP1000A(凸型)', 'img': '1000t'},
                {'name': 'ZP1200A(凸型)', 'img': '1200t'},
                {'name': 'ZP1500A(凸型)', 'img': '1500t'},
                {'name': 'ZP1600A(凸型)', 'img': '1600t'},
                {'name': 'ZP2000A(凸型)', 'img': '2000t'},
                {'name': 'ZP2500A(凸型)', 'img': '2500t'},
                {'name': 'ZP3000A(凸型)', 'img': '3000t'},
                {'name': 'ZP4000A(凸型)', 'img': '4000t'},
                {'name': 'ZP5000A(凸型)', 'img': '5000t'},
                {'name': 'ZP6000A(凸型)', 'img': '6000t'},
                {'name': 'ZP7000A(凸型)', 'img': '7000t'}]

    else:
        return {'ZP200A(凹型)': '200o', 'ZP300A(凹型)': '300o', 'ZP500A(凹型)': '500o', 'ZP800A(凹型)': '800o',
                'ZP1000A(凹型)': '1000o',

                'ZP200A(半凸)': '200b', 'ZP300A(半凸)': '300b', 'ZP500A(半凸)': '500b', 'ZP800A(半凸)': '800b',
                'ZP1000A(半凸)': '1000b',

                'ZP200A(凸型)': '200t', 'ZP300A(凸型)': '300t', 'ZP400A(凸型)': '400t', 'ZP500A(凸型)': '500t',
                'ZP600A(凸型)': '600t', 'ZP800A(凸型)': '800t',
                'ZP1000A(凸型)': '1000t', 'ZP1200A(凸型)': '1200t', 'ZP1500A(凸型)': '1500t', 'ZP2000A(凸型)': '2000t',
                'ZP2500A(凸型)': '2500t', 'ZP3000A(凸型)': '3000t',
                'ZP4000A(凸型)': '4000t', 'ZP5000A(凸型)': '5000t', 'ZP6000A(凸型)': '6000t', 'ZP7000A(凸型)': '7000t'}


def getkspb(munber=1):
    if munber == 1:
        return [{'name': 'KS200A(凹型)', 'img': '200o'},
                {'name': 'KS300A(凹型)', 'img': '300o'},
                {'name': 'KS500A(凹型)', 'img': '500o'},
                {'name': 'KS600A(凹型)', 'img': '600o'},
                {'name': 'KS800A(凹型)', 'img': '800o'},
                {'name': 'KS1000A(凹型)', 'img': '1000o'},
                {'name': 'KS1200A(凹型)', 'img': '1200o'},

                {'name': 'KS200A(凸型)', 'img': '200t'},
                {'name': 'KS300A(凸型)', 'img': '300t'},
                {'name': 'KS500A(凸型)', 'img': '500t'},
                {'name': 'KS600A(凸型)', 'img': '600t'},
                {'name': 'KS800A(凸型)', 'img': '800t'},
                {'name': 'KS1000A(凸型)', 'img': '1000t'},
                {'name': 'KS1200A(凸型)', 'img': '1200t'}]

    else:
        return {'KS200A(凹型)': '200o', 'KS300A(凹型)': '300o', 'KS500A(凹型)': '500o', 'KS600A(凹型)': '600o',
                'KS800A(凹型)': '800o',
                'KS1000A(凹型)': '1000o', 'KS1200A(凹型)': '1200o',

                'KS200A(凸型)': '200t', 'KS300A(凸型)': '300t', 'KS500A(凸型)': '500t', 'KS600A(凸型)': '600t',
                'KS800A(凸型)': '800t', 'KS1000A(凸型)': '1000t', 'KS1200A(凸型)': '1200t'}


def getkapb(munber=1):
    if munber == 1:
        return [{'name': 'KA200A(凹型)', 'img': '200o'},
                {'name': 'KA300A(凹型)', 'img': '300o'},
                {'name': 'KA500A(凹型)', 'img': '500o'},
                {'name': 'KA800A(凹型)', 'img': '800o'},
                {'name': 'KA1000A(凹型)', 'img': '1000o'},

                {'name': 'KA200A(凸型)', 'img': '200t'},
                {'name': 'KA300A(凸型)', 'img': '300t'},
                {'name': 'KA500A(凸型)', 'img': '500t'},
                {'name': 'KA600A(凸型)', 'img': '600t'},
                {'name': 'KA800A(凸型)', 'img': '800t'},
                {'name': 'KA1000A(凸型)', 'img': '1000t'},
                {'name': 'KA1500A(凸型)', 'img': '1500t'}]

    else:
        return {'KA200A(凹型)': '200o', 'KA300A(凹型)': '300o', 'KA500A(凹型)': '500o',
                'KA800A(凹型)': '800o',
                'KA1000A(凹型)': '1000o',

                'KA200A(凸型)': '200t', 'KA300A(凸型)': '300t', 'KA500A(凸型)': '500t', 'KA600A(凸型)': '600t',
                'KA800A(凸型)': '800t', 'KA1000A(凸型)': '1000t', 'KA1500A(凸型)': '1500t'}


def getzkpb(munber=1):
    if munber == 1:
        return [{'name': 'ZK100A(凹型)', 'img': '100o'},
                {'name': 'ZK200A(凹型)', 'img': '200o'},
                {'name': 'ZK300A(凹型)', 'img': '300o'},
                {'name': 'ZK500A(凹型)', 'img': '500o'},
                {'name': 'ZK800A(凹型)', 'img': '800o'},
                {'name': 'ZK1000A(凹型)', 'img': '1000o'},

                {'name': 'ZK200A(凸型)', 'img': '200t'},
                {'name': 'ZK300A(凸型)', 'img': '300t'},
                {'name': 'ZK500A(凸型)', 'img': '500t'},
                {'name': 'ZK800A(凸型)', 'img': '800t'},
                {'name': 'ZK1000A(凸型)', 'img': '1000t'},
                {'name': 'ZK1500A(凸型)', 'img': '1500t'},
                {'name': 'ZK2000A(凸型)', 'img': '2000t'},
                {'name': 'ZK2500A(凸型)', 'img': '2500t'},
                {'name': 'ZK3000A(凸型)', 'img': '3000t'}]

    else:
        return {'ZK100A(凹型)': '100o', 'ZK200A(凹型)': '200o', 'ZK300A(凹型)': '300o', 'ZK500A(凹型)': '500o',
                'ZK800A(凹型)': '800o',
                'ZK1000A(凹型)': '1000o',

                'ZK200A(凸型)': '200t', 'ZK300A(凸型)': '300t', 'ZK500A(凸型)': '500t',
                'ZK800A(凸型)': '800t', 'ZK1000A(凸型)': '1000t', 'ZK1500A(凸型)': '1500t',
                'ZK2000A(凸型)': '2000t', 'ZK2500A(凸型)': '2500t', 'ZK3000A(凸型)': '3000t'}


def getkkpb(munber=1):
    if munber == 1:
        return [
            {'name': 'KK200A(凹型)', 'img': '200o'},
            {'name': 'KK300A(凹型)', 'img': '300o'},
            {'name': 'KK500A(凹型)', 'img': '500o'},
            {'name': 'KK800A(凹型)', 'img': '800o'},
            {'name': 'KK1000A(凹型)', 'img': '1000o'},

            {'name': 'KK200A(凸型)', 'img': '200t'},
            {'name': 'KK300A(凸型)', 'img': '300t'},
            {'name': 'KK500A(凸型)', 'img': '500t'},
            {'name': 'KK600A(凸型)', 'img': '600t'},
            {'name': 'KK800A(凸型)', 'img': '800t'},
            {'name': 'KK1000A(凸型)', 'img': '1000t'},
            {'name': 'KK1200A(凸型)', 'img': '1200t'},
            {'name': 'KK1500A(凸型)', 'img': '1500t'},
            {'name': 'KK2000A(凸型)', 'img': '2000t'},
            {'name': 'KK3000A(凸型)', 'img': '3000t'},
            {'name': 'KK3500A(凸型)', 'img': '3500t'},
            {'name': 'KK4000A(凸型)', 'img': '4000t'},
            {'name': 'KK5000A(凸型)', 'img': '5000t'}]



    else:
        return {'KK200A(凹型)': '200o', 'KK300A(凹型)': '300o', 'KK500A(凹型)': '500o',
                'KK800A(凹型)': '800o',
                'KK1000A(凹型)': '1000o',

                'KK200A(凸型)': '200t', 'KK300A(凸型)': '300t', 'KK500A(凸型)': '500t', 'KK600A(凸型)': '600t',
                'KK800A(凸型)': '800t', 'KK1000A(凸型)': '1000t', 'KK1200A(凸型)': '1200t', 'KK1500A(凸型)': '1500t',
                'KK2000A(凸型)': '2000t', 'KK3000A(凸型)': '3000t', 'KK3500A(凸型)': '3500t', 'KK4000A(凸型)': '4000t',
                'KK5000A(凸型)': '5000t'}


# 整流桥 kbpc  ql sql mdq mds mdst mfq 4zq skbpc


def getkbpc(munber=1):
    if munber == 1:
        return [{'name': 'KBPC10-10', 'img': '10'},
                {'name': 'KBPC15-10', 'img': '15'},
                {'name': 'KBPC20-10', 'img': '20'},
                {'name': 'KBPC25-10', 'img': '25'},
                {'name': 'KBPC30-10', 'img': '30'},
                {'name': 'KBPC35-10', 'img': '35'},
                {'name': 'KBPC50-10', 'img': '50'}]

    else:
        return {'KBPC10-10': '10', 'KBPC15-10': '15', 'KBPC20-10': '20', 'KBPC25-10': '25',
                'KBPC30-10': '30', 'KBPC35-10': '35', 'KBPC50-10': '50'}


def getql(munber=1):
    if munber == 1:
        return [{'name': 'QL10-10', 'img': '10x'},
                {'name': 'QL15-10', 'img': '15x'},
                {'name': 'QL20-10', 'img': '20x'},
                {'name': 'QL25-10', 'img': '25x'},
                {'name': 'QL30-10', 'img': '30x'},
                {'name': 'QL35-10', 'img': '35x'},
                {'name': 'QL50-10', 'img': '50x'},

                {'name': 'QL10A', 'img': '10b'},
                {'name': 'QL20A', 'img': '20b'},
                {'name': 'QL25A', 'img': '25b'},
                {'name': 'QL30A', 'img': '30b'},
                {'name': 'QL35A', 'img': '35b'},
                {'name': 'QL50A', 'img': '50b'},

                {'name': 'QL60A', 'img': '60'},
                {'name': 'QL100A', 'img': '100'},
                {'name': 'QL200A', 'img': '200'},
                {'name': 'QL300A', 'img': '300'}]



    else:
        return {'QL10-10': '10x', 'QL15-10': '15x', 'QL20-10': '20x', 'QL25-10': '25x',
                'QL30-10': '30x', 'QL35-10': '35x', 'QL50-10': '50x',

                'QL10A': '10b', 'QL20A': '20b', 'QL25A': '25b',
                'QL30A': '30b', 'QL35A': '35b', 'QL50A': '50b',

                'QL60A': '60', 'QL100A': '100', 'QL200A': '200',
                'QL300A': '300'}


def getsql(munber=1):
    if munber == 1:
        return [{'name': 'SQL10-10', 'img': '10x'},
                {'name': 'SQL15-10', 'img': '15x'},
                {'name': 'SQL20-10', 'img': '20x'},
                {'name': 'SQL25-10', 'img': '25x'},
                {'name': 'SQL30-10', 'img': '30x'},
                {'name': 'SQL35-10', 'img': '35x'},
                {'name': 'SQL50-10', 'img': '50x'},

                {'name': 'SQL10A', 'img': '10b'},
                {'name': 'SQL20A', 'img': '20b'},
                {'name': 'SQL25A', 'img': '25b'},
                {'name': 'SQL30A', 'img': '30b'},
                {'name': 'SQL35A', 'img': '35b'},
                {'name': 'SQL50A', 'img': '50b'},

                {'name': 'SQL60A', 'img': '60'},
                {'name': 'SQL100A', 'img': '100'},
                {'name': 'SQL200A', 'img': '200'},
                {'name': 'SQL300A', 'img': '300'}]



    else:
        return {'SQL10-10': '10x', 'SQL15-10': '15x', 'SQL20-10': '20x', 'SQL25-10': '25x',
                'SQL30-10': '30x', 'SQL35-10': '35x', 'SQL50-10': '50x',

                'SQL10A': '10b', 'SQL20A': '20b', 'SQL25A': '25b',
                'SQL30A': '30b', 'SQL35A': '35b', 'SQL50A': '50b',

                'SQL60A': '60', 'SQL100A': '100', 'SQL200A': '200',
                'SQL300A': '300'}


def getmdq(munber=1):
    if munber == 1:
        return [{'name': 'MDQ60A', 'img': '60'},
                {'name': 'MDQ100A', 'img': '100'},
                {'name': 'MDQ200A', 'img': '200'},
                {'name': 'MDQ300A', 'img': '300'},
                {'name': 'MDQ500A', 'img': '500'},
                {'name': 'MDQ600A', 'img': '600'},
                {'name': 'MDQ800A', 'img': '800'},
                {'name': 'MDQ1000A', 'img': '1000'},
                {'name': 'MDQ1200A', 'img': '1200'}]
    else:
        return {'MDQ60A': '60', 'MDQ100A': '100', 'MDQ200A': '200', 'MDQ300A': '300',
                'MDQ500A': '500', 'MDQ600A': '600', 'MDQ800A': '800',

                'MDQ1000A': '1000', 'MDQ1200A': '1200'}


def getmds(munber=1):
    if munber == 1:
        return [{'name': 'MDS60A', 'img': '60'},
                {'name': 'MDS100A', 'img': '100'},
                {'name': 'MDS200A', 'img': '200'},
                {'name': 'MDS300A', 'img': '300'},
                {'name': 'MDS500A', 'img': '500'},
                {'name': 'MDS600A', 'img': '600'},
                {'name': 'MDS800A', 'img': '800'},
                {'name': 'MDS1000A', 'img': '1000'},
                {'name': 'MDS1200A', 'img': '1200'}]
    else:
        return {'MDS60A': '60', 'MDS100A': '100', 'MDS200A': '200', 'MDS300A': '300',
                'MDS500A': '500', 'MDS600A': '600', 'MDS800A': '800',

                'MDS1000A': '1000', 'MDS1200A': '1200'}


def getmdst(munber=1):
    if munber == 1:
        return [{'name': 'MDST60A', 'img': '60'},
                {'name': 'MDST100A', 'img': '100'},
                {'name': 'MDST150A', 'img': '150'},
                {'name': 'MDST200A', 'img': '200'}]
    else:
        return {'MDST60A': '60', 'MDST100A': '100', 'MDST150A': '150', 'MDST200A': '200'}


def getmfq(munber=1):
    if munber == 1:
        return [{'name': 'MFQ60A', 'img': '60'},
                {'name': 'MFQ100A', 'img': '100'},
                {'name': 'MFQ200A', 'img': '200'},
                {'name': 'MFQ300A', 'img': '300'}]
    else:
        return {'MFQ60A': '60', 'MFQ100A': '100', 'MFQ200A': '200', 'MFQ300A': '300'}


def getfzq(munber=1):
    if munber == 1:
        return [{'name': '4ZQ10A', 'img': '10'},
                {'name': '4ZQ20A', 'img': '20'},
                {'name': '4ZQ30A', 'img': '30'},
                ]
    else:
        return {'4ZQ10A': '10', '4ZQ20A': '20', '4ZQ30A': '30'}


# 散热器系列
def getsf(munber=1):
    if munber == 1:
        return [{'name': 'SF12', 'img': '12'},
                {'name': 'SF14', 'img': '14'},
                {'name': 'SF15', 'img': '15'},
                {'name': 'SF16', 'img': '16'},
                {'name': 'SF17', 'img': '17'},
                {'name': 'SF18', 'img': '18'}]
    else:
        return {'SF12': '12', 'SF14': '14', 'SF15': '15', 'SF16': '16', 'SF17': '17', 'SF18': '18'}


def getss(munber=1):
    if munber == 1:
        return [{'name': 'SS11', 'img': '11'},
                {'name': 'SS12', 'img': '12'},
                {'name': 'SS13', 'img': '13'},
                {'name': 'SS14', 'img': '14'},
                {'name': 'SS15', 'img': '15'},

                {'name': 'SS11双', 'img': '11s'},
                {'name': 'SS12双', 'img': '12s'},
                {'name': 'SS13双', 'img': '13s'},
                {'name': 'SS14双', 'img': '14s'},
                {'name': 'SS15双', 'img': '15s'}]

    else:
        return {'SS11': '11', 'SS12': '12', 'SS13': '13', 'SS14': '14', 'SS15': '15',
                'SS11双': '11s', 'SS12双': '12s', 'SS13双': '13s', 'SS14双': '14s', 'SS15双': '15s'}


def getlxsr(munber=1):
    if munber == 1:
        return [{'name': 'SL5A', 'img': '5'},
                {'name': 'SL10A', 'img': '10'},
                {'name': 'SL20A', 'img': '20'},
                {'name': 'SL50A', 'img': '50'},
                {'name': 'SL100A', 'img': '100'},
                {'name': 'SL200A', 'img': '200'},
                {'name': 'SL500A', 'img': '500'}]

    else:
        return {'SL5A': '5', 'SL10A': '10', 'SL20A': '20', 'SL50A': '50', 'SL100A': '100',
                'SL200A': '200', 'SL500A': '500'}


# 产品附件

def getfj(munber=1):
    if munber == 1:
        return [{'name': '风机80', 'img': '80'},
                {'name': '风机120', 'img': '120'}]

    else:
        return {'风机80': '80', '风机120': '120'}


def getcfq(munber=1):
    if munber == 1:
        return [{'name': '模块触发器', 'img': 'cfq'}]
    else:
        return {'模块触发器': 'cfq'}

def getnews(munber=0):
    temp = {'title': '新厂区乔迁仪式',
            'content': '2021年8月8日，椿树整流器正式搬迁至新厂区,我们已在半导体行业深耕多年,携手共进是我们矢志的理念,由于过硬的品质,收获广大用户好评。'
                       '此次搬迁后,我们将拾级而上,致力于把更好的产品呈现给用户。',
            'img': ['../static/img/qq_1.jpg', '../static/img/qq_2.jpg', '../static/img/qq_3.jpg',
                    '../static/img/qq_4.jpg'],
            'url': '1000', 'date': '2021-08-15', 'readmunber': '1024'}

    if munber == 1000:
        return temp
    elif munber == 0:
        return [temp]



def getgyjgtjdq(munber=1):
    if munber == 1:
        return [{'name': 'H360-ZF', 'img': '60'},
            {'name': 'H380-ZF', 'img': '80'},
            {'name': 'H3100-ZF', 'img': '100'},
            {'name': 'H3120-ZF', 'img': '120'},
            {'name': 'H3150-ZF', 'img': '150'},
            {'name': 'H3200-ZF', 'img': '200'},
            {'name': 'H3250-ZF', 'img': '250'},
            {'name': 'H3300-ZF', 'img': '300'},
            {'name': 'H3400-ZF', 'img': '400'},
            {'name': 'H3500-ZF', 'img': '500'},
            {'name': 'H3800-ZF', 'img': '800'}]



    else:
        return {'H360-ZF': '60','H380-ZF': '80','H3100-ZF': '100','H3120-ZF': '120','H3150-ZF': '150'
            ,'H3200-ZF': '200','H3250-ZF': '250','H3300-ZF': '300','H3400-ZF': '400','H3500-ZF': '500',
                'H3800-ZF': '800'}
