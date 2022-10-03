# with open('data-20201112-153416.csv', 'r') as f:
#     with open('data-tmp', 'w') as fw:
#         for link in f.readlines():
#             for i, s in enumerate(link.split(', ')):
#                 if i > 0:
#                     fw.write(s)


# Grep the line until first occurence of ;
# grep -Eo "^([^;]+)"

# Get distinct pages
# sed "s/;.*//g" data2.csv | sort | uniq

# with open('links-todo', 'a') as fw:
#     with open('links2-uniq') as fu:
#         uniq = fu.read().split('\n')
#     with open('scraped') as fr:
#         scraped = fr.read().split('\n')

#     for link in uniq:
#         if link not in scraped:
#             fw.write(str(link) + '\n')

# pos = ['greenpeace.international', 'NASAClimateChange', 'bloomberggreen', 'acespace', 'ClimateChangeIsReal',
#       'climatereality', 'ClimateChangeNews', 'NatureClimateChange', 'ClimateChangeCauses', 'GlobalwarmingEva',
#       'MostlyScience', 'EnvironmentandClimateChange', 'TheLeapOrg', 'NatureClimateChange', 'campaigncc',
#       'climatedefenseproject', 'ClimateParents', ]
# neg = ['ClimateChangeLies', 'cfact', 'iloveco2', 'SkepticalScience', 'ccdispatch', 'ClimateDepot', 'LordMonckton']


# pos = ['https://www.facebook.com/greenpeace.international', 'https://www.facebook.com/NASAClimateChange/',
#        'https://www.facebook.com/bloomberggreen/', 'https://www.facebook.com/acespace/',
#        'https://www.facebook.com/ClimateChangeIsReal/', 'https://www.facebook.com/climatereality/',
#        'https://www.facebook.com/ClimateChangeNews', 'https://www.facebook.com/NatureClimateChange',
#        'https://www.facebook.com/ClimateChangeCauses', 'https://www.facebook.com/GlobalwarmingEva']

# neg = ['https://www.facebook.com/cfact', 'https://www.facebook.com/ClimateChangeIsNatural/',
#        'https://www.facebook.com/iloveco2', 'https://www.facebook.com/ClimateChangeLIES/',
#        'https://www.facebook.com/australianclimatemadness', 'https://www.facebook.com/ClimateDepot',
#        'https://www.facebook.com/ccdispatch', 'https://www.facebook.com/TheCO2Coalition',
#        'https://www.facebook.com/Global-Warming-Climate-Change-whatever-its-called-is-a-scam-241741379521',
#        'https://www.facebook.com/Global-Climate-Scam-1392664020945768']


### GENERATE SPLITS BY THE ROOT PAGES
# 'bloomberggreen'
pos = ['NASAClimateChange',
       'acespace', 'greenpeace.international',
       'ClimateChangeIsReal', 'climatereality',
       'ClimateChangeNews', 'NatureClimateChange',
       'ClimateChangeCauses', 'GlobalwarmingEva']

# 'ClimateChangeIsNatural'
neg = ['cfact',
       'iloveco2', 'ClimateChangeLIES',
       'australianclimatemadness', 'ClimateDepot',
       'ccdispatch', 'TheCO2Coalition',
       'Global-Warming-Climate-Change-whatever-its-called-is-a-scam-241741379521',
       'Global-Climate-Scam-1392664020945768']


def add_prefix(prefix, data):
    ret = []
    for l in data:
        ret.append(';'.join([prefix + i.strip() for i in l.split(';') if i]))
    return ret

def append_related(source, target):
    for i in source.split(';'):
        target.append(i.strip())
    return target

prefix = 'https://www.facebook.com/'
ret_pos, ret_neg = [], []
with open('data/data1.csv', 'r') as f1:
    for i, line in enumerate(f1.readlines()):
        init_page = line.split(';', 1)[0].strip()
        if init_page in pos:
            ret_pos.append(line.strip())
            pos = append_related(line, pos)
        if init_page in neg:
            ret_neg.append(line.strip())
            neg = append_related(line, neg)


with open('data/data2-uniq.csv', 'r') as f2:
    for i, line in enumerate(f2.readlines()):
        init_page = line.split(';', 1)[0].strip()
        if init_page in pos:
            ret_pos.append(line.strip())
            pos = append_related(line, pos)
        if init_page in neg:
            ret_neg.append(line.strip())
            neg = append_related(line, neg)


# ret_pos = add_prefix(prefix, ret_pos)
# ret_neg = add_prefix(prefix, ret_neg)

ret_pos_uniq = list(set([ii.strip() for i in ret_pos if i for ii in i.split(';') if ii.strip()]))
ret_neg_uniq = list(set([ii.strip() for i in ret_neg if i for ii in i.split(';') if ii.strip()]))
print('pos: ', len(ret_pos_uniq), ' neg: ', len(ret_neg_uniq))

with open('data/pos_split_uniq.csv', 'w') as fw:
    fw.write('\n'.join(ret_pos_uniq))

with open('data/neg_split_uniq.csv', 'w') as fw:
    fw.write('\n'.join(ret_neg_uniq))

# with open('data/pos.csv', 'w') as fw:
#     fw.write('\n'.join([i for i in ret_pos if i]))

# with open('data/neg.csv', 'w') as fw:
#     fw.write('\n'.join([i for i in ret_neg if i]))

# print(ret_pos)


        