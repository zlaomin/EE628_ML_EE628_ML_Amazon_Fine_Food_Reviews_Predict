# This is the top product id
top_product_id = [
    'B002QWP89S', 'B000KV61FC', 'B004SRH2B6', 'B000EVOSE4', 'B003QNJYXM', 'B0007A0AQW', 'B0018KR8V0', 'B0026RQTGE',
    'B004GW6O9E', 'B0007A0AQM', 'B000GAT6NG', 'B001EO5Q64', 'B000CNB4LE', 'B000KV7ZGQ', 'B000H7LVKY', 'B000NMJWZO',
    'B004EAGP74', 'B004SRFYMK', 'B000ENUC3S', 'B001AS1A4Q', 'B002QWHJOU', 'B000BRR8VQ', 'B008J1HO4C', 'B002QWP8H0',
    'B003CIBPN8', 'B000H0ZJIG', 'B0029ZAOW8', 'B000UBD88A', 'B0018KLPFK', 'B0013A0QXC', 'B003QNLUTI', 'B000H1217M',
    'B000H0ZJHW', 'B001E8DHPW', 'B001EO5U3I'
]

train = [
    'B002QWP89S', 'B000KV61FC', 'B004SRH2B6', 'B000EVOSE4', 'B003QNJYXM', 'B0007A0AQW', 'B0018KR8V0', 'B0026RQTGE',
    'B004GW6O9E', 'B0007A0AQM', 'B000GAT6NG', 'B001EO5Q64', 'B000CNB4LE', 'B000KV7ZGQ', 'B000H7LVKY', 'B000NMJWZO',
    'B004EAGP74', 'B004SRFYMK', 'B000ENUC3S', 'B001AS1A4Q', 'B002QWHJOU', 'B000BRR8VQ', 'B008J1HO4C', 'B002QWP8H0',
    'B003CIBPN8', 'B000H0ZJIG', 'B0029ZAOW8', 'B000UBD88A', 'B0018KLPFK', 'B0013A0QXC', 'B003QNLUTI'
]

test = [
    'B000UBD88A', 'B0018KLPFK', 'B0013A0QXC', 'B003QNLUTI'
]

stopwords = {'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself',
             'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself',
             'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these',
             'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do',
             'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while',
             'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before',
             'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again',
             'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each',
             'few', 'more', 'most', 'other', 'some', 'such', 'only', 'own', 'same', 'so', 'than',
             'too', 'very', 's', 'can', 'will', 'just', 'don', 'should', 'now'}

ori_stopwords = {'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself',
                 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself',
                 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that',
                 'these',
                 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do',
                 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while',
                 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before',
                 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under',
                 'again',
                 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both',
                 'each',
                 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
                 'than',
                 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now'}
