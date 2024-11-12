def is_tg_hash_valid(params: dict) -> bool:
    from config import BOT_TOKEN
    import hashlib
    import hmac

    tg_hash = params['hash']
    check_string = '\n'.join(f'{key}={params[key]}' for key in sorted(params) if key != 'hash')

    secret_key = hashlib.sha256(BOT_TOKEN.encode()).digest()
    hmac_hash = hmac.new(secret_key, msg=check_string.encode(), digestmod=hashlib.sha256).hexdigest()

    return hmac_hash == tg_hash
