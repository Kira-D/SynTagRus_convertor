#!/usr/bin/env python3

""" Custom fixes for sentences.

A sentence must be added to 'patches' in the following structure:
'file_name.conllu': {'sentence_id':
                        {'token_id': {COLUMN_NAME: 'required_value'}
                        }
                    }
"""

import os

input_dir = 'syntagrus-final'
output_dir = 'syntagrus-ultimate'

ID, FORM, LEMMA, UPOS, XPOS, FEAT, HEAD, DEPREL, DEPS, MISC = list(range(10))

patches = {'ru_syntagrus-ud-train.conllu':
                {'2013Budushchee_Medvedeva.xml_33':
                    {'3': {DEPREL: 'conj', DEPS: '5:conj'},
                     '8': {DEPREL: 'root'}
                    },
                 '2009Reforma_obrazovaniya.xml_54':
                    {'9': {HEAD: '7', DEPS: '7:conj'}
                    },
                 '2003Plesnite_koldovstva.xml_66':
                    {'4': {HEAD: '6', DEPS: '6:case', DEPREL: 'case'},
                    '5': {HEAD: '6', DEPS: '6:det', DEPREL: 'det'},
                    '6': {HEAD: '8', DEPS: '8:nmod', DEPREL: 'nmod'}
                    },
                 '2003Sputniki.xml_16':
                    {'12': {HEAD: '13', DEPS: '13:case'},
                    '13': {DEPREL: 'obl'},
                    '14': {HEAD: '13', DEPS: '13:flat:foreign'}
                    },
                 '2008Mars_2.xml_131':
                    {'13': {DEPREL: 'nmod'}
                    },
                 '2008O_boikote_Pekina.xml_11':
                    {'3': {FEAT: 'Case=Acc|Gender=Masc|Number=Sing'}},
                 '2013Zhivut_ne_dlya_radosti.xml_40':
                    {'14': {FEAT: 'Case=Gen|Gender=Fem|Number=Sing'}},
                 '2013Budushchee_Medvedeva.xml_33':
                    {'3': {HEAD: '8', DEPS: '8:punct', DEPREL: 'punct'}},
                 '2011Sverkhkorotkoe_vremya.xml_231':
                    {'5': {UPOS: 'PRON'},
                    '4': {HEAD: '8', DEPS: '8:punct'},
                    '3': {HEAD: '5', DEPS: '8:nsubj', DEPREL: 'nsubj'},
                    },
                 '2011Sverkhkorotkoe_vremya.xml_323':
                    {'22': {HEAD: '23', DEPS: '23:punct'},
                    '23': {HEAD: '21', DEPS: '21:conj'}
                    },
                 '2014Na_dvukh_voinakh_2.xml_225':
                    {'4': {HEAD: '8', DEPS: '8:obl'},
                    '5': {HEAD: '8', DEPS: '8:nsubj'},
                    '7': {HEAD: '8', DEPS: '8:obl'},
                    '8': {HEAD: '0', DEPS: '0:root', DEPREL: 'root'},
                    '9': {HEAD: '8', DEPS: '8:xcomp', DEPREL: 'xcomp'},
                    '12': {HEAD: '8', DEPS: '8:obl'},
                    '16': {HEAD: '8', DEPS: '8:punct'},
                    },
                 'newsYa_18.xml_34':
                    {'19': {HEAD: '18', DEPS: '18:nsubj:pass', DEPREL: 'nsubj:pass'},
                    '20': {HEAD: '19', DEPS: '19:nmod', DEPREL: 'nmod'},
                    '23': {HEAD: '19', DEPS: '19:punct'},
                    '24': {HEAD: '19', DEPS: '19:advcl', DEPREL: 'advcl'},
                    },
                 '2012Stalin_vozvrashchyalsya.xml_1':
                    {'32': {HEAD: '30', DEPS: '30:conj'}},
                 '2011Planerizm.xml_90':
                    {'15': {DEPREL: 'obl', DEPS: '6:obl'}},
                 'newsYa_91.xml_35':
                    {'7': {DEPREL: 'expl', DEPS: '8:expl'}},
                 '2003Somnambula_v_tumane.xml_36':
                    {'23': {DEPREL: 'conj'}
                    },
                 '2007Podkormlennyi_natsizm.xml_98':
                    {'40.1': {DEPS: '35:parataxis'},
                    '42': {DEPREL: 'parataxis'}
                    },
                 '2009EGE.xml_20':
                    {'11.1': {DEPS: '8:parataxis'},
                    '13': {DEPREL: 'parataxis'}
                    },
                 '2009Tranzit_18.xml_98':
                    {'8.1': {DEPS: '5:parataxis'},
                    '7': {DEPREL: 'parataxis'}
                    },
                 '2009Velikaya_pochinka.xml_57':
                    {'3.1': {DEPS: '3:parataxis'},
                    '4': {DEPREL: 'parataxis'}
                    },
                 '2012Problema_vybora.xml_28':
                    {'23.1': {DEPS: '12:parataxis'},
                    '23': {DEPREL: 'parataxis'}
                    },
                 '2012V_konstitutsii_ne_dolzhno_byt_mesta_dlya_vozhdya.xml_194':
                    {'1.1': {DEPS: '1:parataxis'},
                    '6': {DEPREL: 'parataxis'}
                    },
                 '2013Poslednii_dovod_issledovatelya.xml_166':
                    {'20.1': {DEPS: '11:parataxis'},
                    '23': {DEPREL: 'parataxis'}
                    },
                 '2014Vspolokhi-1.xml_113':
                    {'5.1': {DEPS: '3:parataxis'},
                    '6': {DEPREL: 'parataxis'}
                    },
                 'newsMeinert-Ranks.xml_25':
                    {'8.1': {DEPS: '1:parataxis'},
                    '9': {DEPREL: 'parataxis'}
                    },
                 'uppsalaKorp_265.xml_41':
                    {'13.1': {DEPS: '7:parataxis'},
                    '14': {DEPREL: 'parataxis'}
                    },
                },
           'ru_syntagrus-ud-test.conllu':
                {'2011Formula-1.xml_150':
                    {'1': {HEAD: '7', DEPS: '7:nsubj'},
                     '3': {HEAD: '7', DEPS: '7:nummod'},
                     '5': {DEPREL: 'conj', DEPS: '3:conj'},
                     '6': {HEAD: '7', DEPREL: 'amod', DEPS: '7:amod'},
                     '7': {HEAD: '0', DEPREL: 'root', DEPS: '0:root'}
                    },
                 '2011Formula-1.xml_96':
                    {'15.1': {DEPS: '7:conj'},
                    '18': {DEPREL: 'conj'}
                    },
                 '2010Bolezn_rosta.xml_120':
                    {'9.1': {DEPS: '7:parataxis'},
                    '9': {DEPREL: 'parataxis'}
                    },
                },
            'ru_syntagrus-ud-dev.conllu':
                {'uppsalaKorp_619.xml_158':
                    {'9.2': {ID: '9.1'},
                     '11': {DEPS: '9.1:obl'}
                    },
                 '2011Alpinizm.xml_134':
                    {'14.1': {DEPS: '3:parataxis'},
                    '13': {DEPREL: 'parataxis'}
                    },
                 'uppsalaKorp_717.xml_10':
                    {'33.1': {DEPS: '29:parataxis'},
                    '35': {DEPREL: 'parataxis'}
                    },
                 'uppsalaKorp_725.xml_21':
                    {'5.1': {DEPS: '2:parataxis'},
                    '4': {DEPREL: 'parataxis'}
                    },
                 'uppsalaKorp_725.xml_21':
                    {'5.1': {DEPS: '2:parataxis'},
                    '4': {DEPREL: 'parataxis'}
                    },
                }
           }

if __name__ == '__main__':
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for in_file_name in os.listdir(input_dir):
        in_path = os.path.join(input_dir, in_file_name)
        if not in_file_name.endswith('u'):
            in_file_name = in_file_name + 'u'
        out_path = os.path.join(output_dir, in_file_name)

        with open(in_path, 'r', encoding='utf-8') as in_file,\
             open(out_path, 'w', encoding='utf-8') as out_file:
            for line in in_file:
                if line.startswith('# sent_id'):
                    print(line.strip(), file=out_file)
                    sent_id = line.strip().split(' = ')[-1]
                elif line.startswith('#'):
                    print(line.strip(), file=out_file)
                    sent_tokens = []
                elif line == '\n':
                    for token in sent_tokens:
                        token_split = token.split('\t')
                        if in_file_name in patches and sent_id in patches[in_file_name]\
                           and token_split[ID] in patches[in_file_name][sent_id]:
                            for field in patches[in_file_name][sent_id][token_split[ID]]:
                                token_split[field] = patches[in_file_name][sent_id][token_split[ID]][field]
                            token = '\t'.join(token_split)
                        print(token, file=out_file)
                    print(file=out_file)
                else:
                    sent_tokens.append(line.strip())

