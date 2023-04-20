import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Definindo a variável de entrada - Vulnerabilidade
vuln = np.arange(0, 11, 1)
vuln_baixa = fuzz.trimf(vuln, [0, 0, 5])
vuln_media = fuzz.trimf(vuln, [0, 5, 10])
vuln_alta = fuzz.trimf(vuln, [5, 10, 10])

# Definindo a variável de entrada - Conformidade
conf = np.arange(0, 11, 1)
conf_baixa = fuzz.trimf(conf, [0, 0, 5])
conf_alta = fuzz.trimf(conf, [0, 5, 10])

# Definindo a variável de saída - Decisão
decisao = np.arange(0, 11, 1)
decisao_baixa = fuzz.trimf(decisao, [0, 0, 5])
decisao_media = fuzz.trimf(decisao, [0, 5, 10])
decisao_alta = fuzz.trimf(decisao, [5, 10, 10])

# Fuzzificação das entradas
vuln_level_baixa = fuzz.interp_membership(vuln, vuln_baixa, 3)
conf_level_baixa = fuzz.interp_membership(conf, conf_baixa, 7)

# Aplicação das regras fuzzy
active_rule1 = np.fmax(vuln_level_baixa, conf_level_baixa)
agregacao_decisao_baixa = np.fmin(active_rule1, decisao_baixa)

# Defuzzificação
decisao_defuzz = fuzz.defuzz(decisao, agregacao_decisao_baixa, 'centroid')

# Visualização dos resultados
plt.plot(decisao, decisao_baixa, 'b', label='Baixa')
plt.plot(decisao, decisao_media, 'g', label='Média')
plt.plot(decisao, decisao_alta, 'r', label='Alta')
plt.fill_between(decisao, 0, agregacao_decisao_baixa, alpha=0.3)
plt.axvline(x=decisao_defuzz, color='k', linestyle='--', label='Decisão Defuzzificada')
plt.xlabel('Decisão')
plt.ylabel('Pertinência')
plt.title('Gerenciamento de Segurança - Decisão')
plt.legend()
plt.show()












import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Definindo a variável de entrada - Vulnerabilidade
vuln = np.arange(0, 11, 1)
vuln_baixa = fuzz.trimf(vuln, [0, 0, 5])
vuln_media = fuzz.trimf(vuln, [0, 5, 10])
vuln_alta = fuzz.trimf(vuln, [5, 10, 10])

# Definindo a variável de entrada - Conformidade
conf = np.arange(0, 11, 1)
conf_baixa = fuzz.trimf(conf, [0, 0, 5])
conf_alta = fuzz.trimf(conf, [0, 5, 10])

# Definindo a variável de saída - Decisão
decisao = np.arange(0, 11, 1)
decisao_baixa = fuzz.trimf(decisao, [0, 0, 5])
decisao_media = fuzz.trimf(decisao, [0, 5, 10])
decisao_alta = fuzz.trimf(decisao, [5, 10, 10])

# Fuzzificação das entradas
vuln_level_baixa = fuzz.interp_membership(vuln, vuln_baixa, 3)
conf_level_baixa = fuzz.interp_membership(conf, conf_baixa, 7)

# Aplicação das regras fuzzy
active_rule1 = np.fmax(vuln_level_baixa, conf_level_baixa)
agregacao_decisao_baixa = np.fmin(active_rule1, decisao_baixa)

# Defuzzificação
decisao_defuzz = fuzz.defuzz(decisao, agregacao_decisao_baixa, 'centroid')

# Visualização dos resultados
plt.plot(decisao, decisao_baixa, 'b', label='Baixa')
plt.plot(decisao, decisao_media, 'g', label='Média')
plt.plot(decisao, decisao_alta, 'r', label='Alta')
plt.fill_between(decisao, 0, agregacao_decisao_baixa, alpha=0.3)
plt.axvline(x=decisao_defuzz, color='k', linestyle='--', label='Decisão Defuzzificada')
plt.xlabel('Decisão')
plt.ylabel('Pertinência')
plt.title('Gerenciamento de Segurança - Decisão')
plt.legend()
plt.show()












import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Definindo a variável de entrada - Vulnerabilidade
vuln = np.arange(0, 11, 1)
vuln_baixa = fuzz.trimf(vuln, [0, 0, 5])
vuln_media = fuzz.trimf(vuln, [0, 5, 10])
vuln_alta = fuzz.trimf(vuln, [5, 10, 10])

# Definindo a variável de entrada - Conformidade
conf = np.arange(0, 11, 1)
conf_baixa = fuzz.trimf(conf, [0, 0, 5])
conf_alta = fuzz.trimf(conf, [0, 5, 10])

# Definindo a variável de saída - Decisão
decisao = np.arange(0, 11, 1)
decisao_baixa = fuzz.trimf(decisao, [0, 0, 5])
decisao_media = fuzz.trimf(decisao, [0, 5, 10])
decisao_alta = fuzz.trimf(decisao, [5, 10, 10])

# Fuzzificação das entradas
vuln_level_baixa = fuzz.interp_membership(vuln, vuln_baixa, 3)
conf_level_baixa = fuzz.interp_membership(conf, conf_baixa, 7)

# Aplicação das regras fuzzy
active_rule1 = np.fmax(vuln_level_baixa, conf_level_baixa)
agregacao_decisao_baixa = np.fmin(active_rule1, decisao_baixa)

# Defuzzificação
decisao_defuzz = fuzz.defuzz(decisao, agregacao_decisao_baixa, 'centroid')

# Visualização dos resultados
plt.plot(decisao, decisao_baixa, 'b', label='Baixa')
plt.plot(decisao, decisao_media, 'g', label='Média')
plt.plot(decisao, decisao_alta, 'r', label='Alta')
plt.fill_between(decisao, 0, agregacao_decisao_baixa, alpha=0.3)
plt.axvline(x=decisao_defuzz, color='k', linestyle='--', label='Decisão Defuzzificada')
plt.xlabel('Decisão')
plt.ylabel('Pertinência')
plt.title('Gerenciamento de Segurança - Decisão')
plt.legend()
plt.show()












import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Definindo a variável de entrada - Vulnerabilidade
vuln = np.arange(0, 11, 1)
vuln_baixa = fuzz.trimf(vuln, [0, 0, 5])
vuln_media = fuzz.trimf(vuln, [0, 5, 10])
vuln_alta = fuzz.trimf(vuln, [5, 10, 10])

# Definindo a variável de entrada - Conformidade
conf = np.arange(0, 11, 1)
conf_baixa = fuzz.trimf(conf, [0, 0, 5])
conf_alta = fuzz.trimf(conf, [0, 5, 10])

# Definindo a variável de saída - Decisão
decisao = np.arange(0, 11, 1)
decisao_baixa = fuzz.trimf(decisao, [0, 0, 5])
decisao_media = fuzz.trimf(decisao, [0, 5, 10])
decisao_alta = fuzz.trimf(decisao, [5, 10, 10])

# Fuzzificação das entradas
vuln_level_baixa = fuzz.interp_membership(vuln, vuln_baixa, 3)
conf_level_baixa = fuzz.interp_membership(conf, conf_baixa, 7)

# Aplicação das regras fuzzy
active_rule1 = np.fmax(vuln_level_baixa, conf_level_baixa)
agregacao_decisao_baixa = np.fmin(active_rule1, decisao_baixa)

# Defuzzificação
decisao_defuzz = fuzz.defuzz(decisao, agregacao_decisao_baixa, 'centroid')

# Visualização dos resultados
plt.plot(decisao, decisao_baixa, 'b', label='Baixa')
plt.plot(decisao, decisao_media, 'g', label='Média')
plt.plot(decisao, decisao_alta, 'r', label='Alta')
plt.fill_between(decisao, 0, agregacao_decisao_baixa, alpha=0.3)
plt.axvline(x=decisao_defuzz, color='k', linestyle='--', label='Decisão Defuzzificada')
plt.xlabel('Decisão')
plt.ylabel('Pertinência')
plt.title('Gerenciamento de Segurança - Decisão')
plt.legend()
plt.show()












import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Definindo a variável de entrada - Vulnerabilidade
vuln = np.arange(0, 11, 1)
vuln_baixa = fuzz.trimf(vuln, [0, 0, 5])
vuln_media = fuzz.trimf(vuln, [0, 5, 10])
vuln_alta = fuzz.trimf(vuln, [5, 10, 10])

# Definindo a variável de entrada - Conformidade
conf = np.arange(0, 11, 1)
conf_baixa = fuzz.trimf(conf, [0, 0, 5])
conf_alta = fuzz.trimf(conf, [0, 5, 10])

# Definindo a variável de saída - Decisão
decisao = np.arange(0, 11, 1)
decisao_baixa = fuzz.trimf(decisao, [0, 0, 5])
decisao_media = fuzz.trimf(decisao, [0, 5, 10])
decisao_alta = fuzz.trimf(decisao, [5, 10, 10])

# Fuzzificação das entradas
vuln_level_baixa = fuzz.interp_membership(vuln, vuln_baixa, 3)
conf_level_baixa = fuzz.interp_membership(conf, conf_baixa, 7)

# Aplicação das regras fuzzy
active_rule1 = np.fmax(vuln_level_baixa, conf_level_baixa)
agregacao_decisao_baixa = np.fmin(active_rule1, decisao_baixa)

# Defuzzificação
decisao_defuzz = fuzz.defuzz(decisao, agregacao_decisao_baixa, 'centroid')

# Visualização dos resultados
plt.plot(decisao, decisao_baixa, 'b', label='Baixa')
plt.plot(decisao, decisao_media, 'g', label='Média')
plt.plot(decisao, decisao_alta, 'r', label='Alta')
plt.fill_between(decisao, 0, agregacao_decisao_baixa, alpha=0.3)
plt.axvline(x=decisao_defuzz, color='k', linestyle='--', label='Decisão Defuzzificada')
plt.xlabel('Decisão')
plt.ylabel('Pertinência')
plt.title('Gerenciamento de Segurança - Decisão')
plt.legend()
plt.show()












import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Definindo a variável de entrada - Vulnerabilidade
vuln = np.arange(0, 11, 1)
vuln_baixa = fuzz.trimf(vuln, [0, 0, 5])
vuln_media = fuzz.trimf(vuln, [0, 5, 10])
vuln_alta = fuzz.trimf(vuln, [5, 10, 10])

# Definindo a variável de entrada - Conformidade
conf = np.arange(0, 11, 1)
conf_baixa = fuzz.trimf(conf, [0, 0, 5])
conf_alta = fuzz.trimf(conf, [0, 5, 10])

# Definindo a variável de saída - Decisão
decisao = np.arange(0, 11, 1)
decisao_baixa = fuzz.trimf(decisao, [0, 0, 5])
decisao_media = fuzz.trimf(decisao, [0, 5, 10])
decisao_alta = fuzz.trimf(decisao, [5, 10, 10])

# Fuzzificação das entradas
vuln_level_baixa = fuzz.interp_membership(vuln, vuln_baixa, 3)
conf_level_baixa = fuzz.interp_membership(conf, conf_baixa, 7)

# Aplicação das regras fuzzy
active_rule1 = np.fmax(vuln_level_baixa, conf_level_baixa)
agregacao_decisao_baixa = np.fmin(active_rule1, decisao_baixa)

# Defuzzificação
decisao_defuzz = fuzz.defuzz(decisao, agregacao_decisao_baixa, 'centroid')

# Visualização dos resultados
plt.plot(decisao, decisao_baixa, 'b', label='Baixa')
plt.plot(decisao, decisao_media, 'g', label='Média')
plt.plot(decisao, decisao_alta, 'r', label='Alta')
plt.fill_between(decisao, 0, agregacao_decisao_baixa, alpha=0.3)
plt.axvline(x=decisao_defuzz, color='k', linestyle='--', label='Decisão Defuzzificada')
plt.xlabel('Decisão')
plt.ylabel('Pertinência')
plt.title('Gerenciamento de Segurança - Decisão')
plt.legend()
plt.show()












import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Definindo a variável de entrada - Vulnerabilidade
vuln = np.arange(0, 11, 1)
vuln_baixa = fuzz.trimf(vuln, [0, 0, 5])
vuln_media = fuzz.trimf(vuln, [0, 5, 10])
vuln_alta = fuzz.trimf(vuln, [5, 10, 10])

# Definindo a variável de entrada - Conformidade
conf = np.arange(0, 11, 1)
conf_baixa = fuzz.trimf(conf, [0, 0, 5])
conf_alta = fuzz.trimf(conf, [0, 5, 10])

# Definindo a variável de saída - Decisão
decisao = np.arange(0, 11, 1)
decisao_baixa = fuzz.trimf(decisao, [0, 0, 5])
decisao_media = fuzz.trimf(decisao, [0, 5, 10])
decisao_alta = fuzz.trimf(decisao, [5, 10, 10])

# Fuzzificação das entradas
vuln_level_baixa = fuzz.interp_membership(vuln, vuln_baixa, 3)
conf_level_baixa = fuzz.interp_membership(conf, conf_baixa, 7)

# Aplicação das regras fuzzy
active_rule1 = np.fmax(vuln_level_baixa, conf_level_baixa)
agregacao_decisao_baixa = np.fmin(active_rule1, decisao_baixa)

# Defuzzificação
decisao_defuzz = fuzz.defuzz(decisao, agregacao_decisao_baixa, 'centroid')

# Visualização dos resultados
plt.plot(decisao, decisao_baixa, 'b', label='Baixa')
plt.plot(decisao, decisao_media, 'g', label='Média')
plt.plot(decisao, decisao_alta, 'r', label='Alta')
plt.fill_between(decisao, 0, agregacao_decisao_baixa, alpha=0.3)
plt.axvline(x=decisao_defuzz, color='k', linestyle='--', label='Decisão Defuzzificada')
plt.xlabel('Decisão')
plt.ylabel('Pertinência')
plt.title('Gerenciamento de Segurança - Decisão')
plt.legend()
plt.show()












import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Definindo a variável de entrada - Vulnerabilidade
vuln = np.arange(0, 11, 1)
vuln_baixa = fuzz.trimf(vuln, [0, 0, 5])
vuln_media = fuzz.trimf(vuln, [0, 5, 10])
vuln_alta = fuzz.trimf(vuln, [5, 10, 10])

# Definindo a variável de entrada - Conformidade
conf = np.arange(0, 11, 1)
conf_baixa = fuzz.trimf(conf, [0, 0, 5])
conf_alta = fuzz.trimf(conf, [0, 5, 10])

# Definindo a variável de saída - Decisão
decisao = np.arange(0, 11, 1)
decisao_baixa = fuzz.trimf(decisao, [0, 0, 5])
decisao_media = fuzz.trimf(decisao, [0, 5, 10])
decisao_alta = fuzz.trimf(decisao, [5, 10, 10])

# Fuzzificação das entradas
vuln_level_baixa = fuzz.interp_membership(vuln, vuln_baixa, 3)
conf_level_baixa = fuzz.interp_membership(conf, conf_baixa, 7)

# Aplicação das regras fuzzy
active_rule1 = np.fmax(vuln_level_baixa, conf_level_baixa)
agregacao_decisao_baixa = np.fmin(active_rule1, decisao_baixa)

# Defuzzificação
decisao_defuzz = fuzz.defuzz(decisao, agregacao_decisao_baixa, 'centroid')

# Visualização dos resultados
plt.plot(decisao, decisao_baixa, 'b', label='Baixa')
plt.plot(decisao, decisao_media, 'g', label='Média')
plt.plot(decisao, decisao_alta, 'r', label='Alta')
plt.fill_between(decisao, 0, agregacao_decisao_baixa, alpha=0.3)
plt.axvline(x=decisao_defuzz, color='k', linestyle='--', label='Decisão Defuzzificada')
plt.xlabel('Decisão')
plt.ylabel('Pertinência')
plt.title('Gerenciamento de Segurança - Decisão')
plt.legend()
plt.show()












