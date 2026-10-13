import pandas as pd

df = pd.read_excel('dados_pesquisa_seduc/pesquisa_seduc_formatado.xlsx')

# print(df)

# Printar tipos de ensino distintos
print(df['Tipo_de_Ensino'].unique())
[                                                    'OUTRAS',
                                     'PRIVADA - FILANTRÓPICA',
                'EDUCAÇÃO PROFISSIONAL - QUALIFICAÇÃO BÁSICA',
                 'Escola Exclusiva de Atividade Complementar',
                                       'EE (ESCOLA ESTADUAL)',
                                        'PRIVADA COMUNITÁRIA',
                                                        'CEL',
                                                'FEBEM - UIP',
                                                 'FEBEM - UI',
                                       'EDUCAÇÃO A DISTÂNCIA',
                                          'CLASSE HOSPITALAR',
                                                      'SENAI',
                                          'SCT - PAULA SOUZA',
                                             'EAD/PRESENCIAL',
                                       'CLASSE PENITENCIÁRIA',
                                                      'SENAC',
                                                  'SESI - CE',
                           'Paula Souza - Ensino a distância',
 'CIEJA â€“ CENTRO INTEGRADO DE EDUCAÇÃO DE JOVENS E ADULTOS',
                                                        'USP',
                                                        'CCI',
                                              'CEFOR - SAUDE',
                                   'SENAI - DISTÂNCIA/BÁSICA',
                                   'PRIVADA â€“ CONFESSIONAL',
                                                      'CEEJA',
                             'EEI (ESCOLA ESTADUAL INDÍGENA)',
                                'PROEJA - ENSINO FUNDAMENTAL']

escolas_EM = []

