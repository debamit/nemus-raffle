from ens.auto import ns

def is_eth_handle(ens_handle:str) -> bool:
    if ens_handle:
        return bool(ens_handle.endswith(".eth"))

def address_lookup(ens_handle:str) -> str:
    if is_eth_handle(ens_handle):
        return ns.address(ens_handle)
    return ens_handle

ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])