# -*- coding: utf-8 -*-

# 文件最大大小
FILE_MAX_SIZE = 5 * 1024 * 1024

# 文件大小不合法提示消息
FILE_SIZE_INVALID_MSG = f"File size must < {FILE_MAX_SIZE} bytes"

####################
# 手机号相关
####################

# 国内手机号
MOBILE_PHONE = 'mobile_phone'

# 国内固定电话
FIXED_TELEPHONE = 'fixed_telephone'

# 默认匹配的号码类型
DEFAULT_PHONE_TYPE = MOBILE_PHONE

# 号码类型不支持提示消息
PHONE_TYPE_UNSUPPORTED_MSG = 'phone type unsupported: {phone_type}'

# 号码无匹配提示消息
NO_PHONE_MATCHED_MSG = "No Phone Matched"

# 号码匹配默认提示消息
DEFAULT_PHONE_MATCHED_MSG = "[Line: {line}] phone matched: {phone}"

# 国内手机号匹配提示消息
MOBILE_PHONE_MATCHED_MSG = "[Line: {line}] mobile_phone matched: {phone}"

# 国内固定电话匹配提示消息
FIXED_TELEPHONE_MATCHED_MSG = '[Line: {line}] fixed telephone matched: {phone}'


####################
# 地址相关
####################

# 地址无匹配提示消息
NO_ADDRESS_MATCHED_MSG = "No AddressMatchedData Matched"

# 地址匹配提示消息
ADDRESS_MATCHED_MSG = "[Line: {line}] address matched: {address}"
