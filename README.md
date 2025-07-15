criar em python um identificador de lead score, quando o lead entra no crm ele já entra com as seguintes informações preenchidas: segmento da empresa, cargo e número de licenças. A ideia é que cada uma dessas questões entre com um 'peso', ao somar todos os pesos gera um lead score. Essas automações entre o crm e a captação do lead ocorrem através do n8n, logo, depois de fazer o script em python, preciso criar o campo de score e também adaptar o crm para receber este campo personalizado.

O primeiro passo que quero realizar é criar o script em python, para isso eu preciso transformar os campos 'segmento da empresa', 'cargo', 'número de licenças' em números. Os dois primeiros campos recebem o valor de string, mas preciso definir que os campos, vamos definir os 6 principais, retornarem pontuações diferentes, e os demais, quando selecionados, recebem um valor padrão. Por exemplo, identifiquei no banco de dados que a lista com os segmentos de empresas que mais são clientes são: 1º - Software e Cloud; 2º - Comércio; 3º - Serviços em geral;  4º - Serviços e Estética; 5º - Industria Geral; 6º - Financeiro e Serviços Relacionados.

Baseado nisso, conforme o lead escolher uma dessas opções ele recebe uma pontuação interna variada, 1º lugar recebe pontuação mais alta que o 6º, qualquer um que não for entre um destes seis, recebe um valor menor que o 6º lugar, e fixo. Essa pontuação do 'segmento da empresa' vai corresponder a 15% do valor total.

Na segunda parte do script tem o 'cargo' do usuário que está fazendo cadastro, no banco de dados foram identificados os cargos que mais tem licenças, que são: 1º - gerente; 2º - diretor; 3º - analista; 4º -  coordenador; 5º - supervisor; 6º - assistente. Novamente, o 1º lugar recebe o valor mais alto enquanto o 6º lugar recebe o valor mais baixo, qualquer escolha que não seja essas recebe um valor menor que o 6º lugar e fixo. Essa parte deve corresponder a 15% do valor total

Na terceira parte 'quantidade de licenças' terá os campos de escolha, 1 a 3 licenças; 4 a 8 licenças; 9 a 15 licenças; acima de 15 licenças. O campo marcado entre '1 a 3 licenças' deve receber o valor mais baixo, enquanto o campo 'acima de 15' deve receber o valor mais alto. Essa parte deve corresponder a 70% do valor total. 

Ou seja, dentro de cada parte vai corresponder a uma %, que somando todas as % vai ganhar um score final.
Este score deve ser definido assim, leads que receberam o score até 20 é um lead frio, leads que ficaram entre 20 e 50 é um lead morno. Leads que ficaram com o score final com mais de 50 é um lead quente e leads que ficaram com score com mais de 80 é um lead muito quente.

Dessa forma, quero que primeiro, antes do script, você me ajude a pensar se a ideia, a lógica por tras do programa está correta, estou estudando python então ainda estou treinando essa visão. Quero ajuda para definir estar % separadas e no total, para o leadscore fazer sentido. Posteriormente trabalhamos o resto do script.

___
Dica 1: para deixar o sistema mais flexível futuramente pode parametrizar esses pesos em um dicionário, assim pode ajustá-los sem alterar o código.

- **Segmento da empresa → 15%**
    
- **Cargo do contato → 15%**
    
- **Número de licenças → 70%**

**Segmento da empresa (15 pontos):**

- Software e Cloud → 15
    
- Comércio → 13
    
- Serviços em geral → 11
    
- Serviços e Estética → 9
    
- Indústria Geral → 7
    
- Financeiro e Serviços Relacionados → 5
    
- Outros → 3 (valor fixo)
    

**Cargo do contato (15 pontos):**

- Gerente → 15
    
- Diretor → 13
    
- Analista → 11
    
- Coordenador → 9
    
- Supervisor → 7
    
- Assistente → 5
    
- Outros → 3 (valor fixo)
    

**Quantidade de licenças (70 pontos):**

- 1 a 3 → 10
    
- 4 a 8 → 30
    
- 9 a 15 → 50
    
- Acima de 15 → 70

**Lead Score**
-  ≤ 30 → Frio  
    
- 31–60 → Morno  
    
- 61–80 → Quente  
    
- 81+ → Muito Quente
