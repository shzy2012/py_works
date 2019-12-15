# -*- coding: utf-8 -*-


MOBIL_PHONE_PATTERN = r'(?<!\d)(?:[\(|（]\s*\+?86\s*[\)|）]\s*|\s*\+86\s*)?(1(?:[3589]\d{9}|[4][5-9]{8}|[6][124-7]{8}|[7][0-8]{8}))(?!\d)'

FIXED_TELEPHONE_PATTERN = r'(?<!\d)(?:[\(|（]\s*\+?86\s*[\)|）]\s*|\s*\+86\s*)?(0(((31|35|47|51|53|55|57|71|75|77|79|83|87|93|99)\d|335|349|37[0-79]|39[1-68]|41[125-9]|42[179]|43[1-9]|45[1-9]|46[47-9]|48[23]|52[37]|54[36]|56[1-46]|580|59[1-9]|63[1-5]|66[0238]|69[12]|701|72[248]|73[014-9]|74[3-6]|76[023689]|81[23678]|82[5-7]|85[14-9]|88[3678]|89[1-8]|90[123689]|91[1-679]|94[13]|95[1-5]|97[0-79])\s*\-?\s*\d{7}|(10|2\d)\s*\-?\s*\d{8}))(?!\d)'

ADDRESS_PATTERN = r'(.*?[省|市|自治区|特别行政区])(.*?[市|市辖区|地区|盟|自治州])?(.*?[市|县|区|新城|旗])(.*?[乡|镇|办事处])?(.*?[小区|村|路])(.*?[组|号|弄])(.*?[号楼|幢|楼|栋|室])?(.*?[室])?'

# 十五位身份证号表达式 identity_util
ID_NUMBER_15_REGEX = r'((?<!\d)[1-9]\d{5}\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}(?!\d))'

# 十八位身份证号表达式 identity_util
ID_NUMBER_18_REGEX = r'((?<!\d)[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx](?!\d))'
