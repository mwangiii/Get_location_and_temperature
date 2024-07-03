def get_ip(req):
    ip = req.headers.get('x-forwarded-for') or req.remote_addr or req.environ.get('REMOTE_ADDR') or None
    if ip and ',' in ip:
        ip = ip.split(',')[0]
    if ip and ip.startswith('::ffff:'):
        ip = ip[7:]
    return ip
