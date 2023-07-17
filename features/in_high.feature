Feature: Em Alta

    A feature destaca as 10 músicas mais repercutidas da última semana, fornecendo aos usuários uma visão atualizada das tendências musicais e permitindo que eles descubram novas músicas populares e interessantes.

Scenario: Exibir informações sobre as músicas em alta
GIVEN que o usuário “Ana” está na página de “Reviews” 
WHEN o usuário “Ana” clicar no “Em alta”
THEN o usuário “Ana” deve ser redirecionado à uma página de “Em alta”
AND o usuário “Ana” deve visualizar uma lista das músicas em alta com algumas informações sobre a música (título, cantor, capa do álbum)

Scenario: Filtrar músicas em alta por gênero musical
GIVEN que o usuário “Ana” está na página de “Em alta” 
AND que existem músicas disponíveis no sistema
WHEN o usuário “Ana” clicar no ícone “filtros”
AND escolher um gênero musical dentre as opções listadas
THEN o usuário “Ana” deve ser redirecionado à uma nova página com uma lista das músicas em alta apenas no gênero selecionado

Scenario: Busca por gênero musical
GIVEN o usuário “Ana” está na página de “Reviews”
AND o usuário “Ana” quer achar a review de uma música “Cruel Summer” do género POP
WHEN o usuário “Ana” clica no “filtro” de busca
AND o usuário “Ana” escolhe o gênero POP na categoria de “Gêneros” no filtro
THEN é exibida uma lista de resultados onde ela visualiza a música de título " “Cruel Summer"