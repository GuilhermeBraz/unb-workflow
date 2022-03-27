# UnB / Eng Software / FRC / Turma 2021.2 / Prof. Fernando W Cruz

# Lista de Exercícios

**1. Porque o software de rede é dividido em camadas?**
2. Quais as diferenças entre a arquitetura TCP/IP e a RM-OSI/ISO?
    -  OSI has 7 layers whereas TCP/IP has 4 layers.
    - The OSI Model is a logical and conceptual model that defines network communication used by systems open to interconnection and communication with other systems. On the other hand, TCP/IP helps you to determine how a specific computer should be connected to the internet and how you can be transmitted between them.
    -   OSI header is 5 bytes whereas TCP/IP header size is 20 bytes.
    -   OSI refers to Open Systems Interconnection whereas TCP/IP refers to Transmission Control Protocol.
    -   OSI follows a vertical approach whereas TCP/IP follows a horizontal approach.
    -   OSI model, the transport layer, is only connection-oriented whereas the TCP/IP model is both connection-oriented and connectionless.
    -  OSI model is developed by ISO (International Standard Organization), whereas TCP Model is developed by ARPANET (Advanced Research Project Agency Network).
	-   OSI model helps you to standardize router, switch, motherboard, and other hardware whereas TCP/IP helps you to establish a connection between different types of computers.
3. O que é padrão de facto e padrão de juri?
4. O que é uma PDU?
   PDU (Protocol Data Unit), se refere as unidades basicas de dados pelas camadas OSI
   1.  Camada física - bruta [pedaços](https://techlib.wiki/definition/bit.html) (1s ou 0s) transmitidos fisicamente através do [Hardware](https://techlib.wiki/definition/hardware.html)
   2.  Camada Data Link - um quadro (ou série de bits) 
   3.  Camada de rede - um [pacote](https://techlib.wiki/definition/packet.html) que contém o endereço de origem e destino
   4.  Camada de transporte - um segmento que inclui um [TCP](https://techlib.wiki/definition/tcp.html) cabeçalho e datra
   5.  Camada de sessão - os dados passados  para a conexão de rede
   6.  Camada de apresentação - os dados formatados para apresentação
   7.  Camada de aplicação - os dados recebidos ou transmitidos por um software [aplicação](https://techlib.wiki/definition/application.html)
**5. O que é primitiva de serviço?**
6. Qual a definição de protocolo de comunicação?
7. O que é um serviço orientado à conexão? E um serviço não orientado à conexão?
8. Qual a diferença entre a largura de banda do meio físico e a largura de banda do sinal? Se o primeiro for maior do que o segundo, é possível comportar mais de um tipo de sinal? Que tipo de estratégias é possível usar para viabilizar isso (mais de um sinal no mesmo meio físico)?
9. Para que servem os modems?
    Modular e demodular sinais analogicos em digitais e vice versa.
10. Quais as diferenças entre modulação ASK, FSK e PSK?
	Todos sao metodos de modulacao digital(digital modulation)
	- ASK (Amplitude shifting keying): muda a amplitude da onda analogica de acordo com 0 e 1, diminuindo com 0 e maior com 1.
	- FSK (Frequencie shifting keying): muda a frequencia da onda de acordo com 0 e 1, diminuindo com 0 e maior com 1.
	- PSK (Phase shifiting keying): muda a fase no ponto de transicao de 0 -> 1 e 1 -> 0
11. Qual a relação entre largura de banda e taxa de transmissão?
12. O que é elemento de sinal em transmissões? O que é baud? Como representar os bits em
    transmissões usando moedas? Como se consegue uma taxa de 28800 bps num modem?
13. Qual a diferença entre um multiplexador TDM e um multiplexador FDM?
14. Qual a diferença entre meio físico guiado e não guiado?
15. Quais as taxas de transmissão e qual padrão de rede local fazem uso de cabo coaxial?
16. Explique qual a diferença entre uma rede local com cabeamento estruturado e uma rede sem
    esse tipo de cabeamento. Qual a importância dessa estratégia na montagem de redes locais?
17. Faça um quadro comparativo sobre os cabos par trançado usados em redes locais e telefonia,
    com destaque para os cabos e conectores categorias 1, 3, 5, 6 (comentar taxa de
    transmissão, tipo de redes em que são usados, largura de banda, tipo de transmissão mais
    apropriada, etc.)
18. Qual a diferença entre fibras monomodo e multimodo?
19. Explique, em linhas gerais, como funciona o protocolo RS-
20. Explique as diferenças entre redes de comutação de circuito e comutação de pacotes.
21. Explique como funcionam os CODECs
**22. Explique a técnica PCM e a técnica PAM (Pulse Amplitude Modulation) usada para conversão de fontes analógicas em informações digitais.**
      - PCM : Dividido em tres fases sampling, quantizing e encoding. Na fase de sampling o sinal eh dividido em cortes verticais em intervalos regulares; na fase de quantizing eh feito a divisao em linhas horizontais combinando com as verticais, criando um sinal digital ali dentro dentro dos niveis; entao na fase de encoding eh feito a conversao dessas samples em binario.
**23. Quais as funcionalidades da camada de enlace de dados?**
      - Atribuir headers e tails no PDU ou frame como referido na camada 2, para poder comunicar com os MACS na LAN
24. Porque é preciso enquadrar os bits na camada de enlace de dados? Que técnicas são usadas para enquadramento?
25. Quais os mecanismos de controle de erros mais comuns em uso?
26. Explique o que é distância de Hamming em sistemas de transmissão.
27. Explique como funciona a técnica de CRC e paridade longitudinal, para correção de erros
28. Explique como funciona o protocolo stop-and-wait.
29. O que é o conceito de piggybacking usando em protocolos de enlace ponto-a-ponto? Como
ele é implementado?
30. Qual a relação entre o número de bits usados para numerar os quadros e o tamanho da janela
de transmissão?
31. Qual a diferença entre os mecanismos de retransmissão seletiva e go-back-N?
32. Qual a diferença entre janela de transmissão e janela de recepção nos protocolos de janela
deslizante?
33. Considere um protocolo de transmissão ponto-a-ponto (enlace de dados), com janela de ransmissão igual a 5 entre dois hosts. Suponha que, ao transmitir, o quadro 2 se perde. Comoesse protocolo se comporta para restabelecer esse quadro, considerando o mecanismo go-back-N? E se fosse retransmissão seletiva?
34. Explique quais foram as mudanças efetuadas no Ethernet a (10Mbps) para criação do
FastEthernet (100Mbps) e de outras variações de mais alta velocidade
35. Explique as diferenças entre o mecanismos de acesso ao meio utilizados em redes WiFi e em redes cabeadas... Porque o mecanismo definido é diferente nesses dois tipos de tecnologias?
36. Mostre o quadro Ethernet/IEEE802.3, explicando cada um dos seus campos. Porque um
quadro precisa ter um tamanho mínimo? Porque precisa ter um tamanho máximo?
37. O que é endereço MAC? O que é endereçamento unicast, multicast e Broadcast?
38. Quais as diferenças entre redes Simplex, half-duplex e full-duplex?
39. Em redes Ethernet, o método de acesso ao meio é não determinístico, diferente do que ocorre em redes de comunicação que fazem uso de multiplexadores TDM. Ou seja, o Ethernet pode ser visto com o um TDM assíncrono (não baseado em relógio). Julgue essa afirmação informando se está certa ou errada. Justifique sua resposta.
40. Explique, em linhas gerais, como funciona o padrão IEEE802.5/Token Ring, com destaque para formato do quadro.
41. O Token Ring é um protocolo com acesso ao meio determinístico ou não? Justifique sua
resposta.
42. Explique como as estações de trabalho conseguem saber a diferença entre um token e um quadro de informações.
43. Quais as diferenças entre uma rede local Ethernet e uma rede local Token Ring?
44. Mostre o formato de um quadro típico de uma rede IEEE802.11, explicando a funcionalidade de seus campos.


