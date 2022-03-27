## Exemplos de softwares de rede
1. Rede SNS (IBM) - Modelo em 6 camadas
2. Rede DECNet (Digital) - Modelo em 4 camadas
3. Rede Netware (Novell) - Modelo em 4 camadas
4. Rede TCP/IP (Open Source) - Modelo em 4 camadas (camada IP, camada TCP/UDP e camada de aplicação (http, DNS SMTP, etc) )

## Bandwith, throughtput and speed
- Bandwith: maximum ammount of data transfer per second (10gbps)
>Bandwith can also mean the range of frequencies used to transmit signal (Hz)
- Throughtput: real ammount of data being transfered through the media/connection
- Speed: often refers to the amount of data that can be downloaded/uploaded in a specific connection

## Baseband x Broadband 
- Baseband refers to digital signal transmisison, where the entire bandwith of the medium is used for one signal. (Ex: ethernet)
	- Uses TDM (Time Division Multiplexing)
> Can also refers to the base frequencie range of the original analog singnal before its modulated to a different frequent range
- Broadband refers to any type of signal transmission that shares the medium with two or more different types of data in separate channels (analog)
	- Uses FDM (Frequencie Division Multiplexing)

- Table of diferences
	
| Factor | Baseband | Broadband |
|---|---|---|
| The signal used for transmission. | The baseband transmits the digital signal using the physical medium like wires. | The broadband transmits the analog signals using optical fibers and twisted cables as a medium of transmission. |
| Transmission direction | The baseband signaling is termed as bidirectional and is capable of sending digital signals in both directions. | The broadband signaling is termed as bidirectional and is capable of sending digital signals in only one direction. |
| Encoding scheme used | The baseband signaling used Manchester encoding scheme while transmitting the digital signals. | The broadband signaling used Manchester encoding scheme while transmitting the analog signals. |
| Range of signals | The baseband transmission can transmit the digital signals over a short distance only when compared to broadband transmission. If the digital signals need to be transmitted for a long distance, the attenuation process is required. | The broadband transmission can transmit the analog signals over a long distance compared to baseband transmission, and for transmitting the signals, no need for attenuation technique is required. |
| Topology used | The baseband transmission uses the bus topology as the application. | The broadband transmission uses the tree and bus topology as the application. |
| A number of data streams transmitted. | The baseband transmission can transmit the single data type stream at one glance and can send in bidirectional. | The broadband transmission can transmit multiple data streams at the same time but in one direction only. |
| Medium of transfer | The baseband signals used twisted-pair cables, coaxial cables and wires as a medium of transmitting digital signals. | The broadband signals used optical fiber cables, coaxial cables, and radio waves to transmit the analog signals. |
| Application | The baseband transmission is mostly used for the LAN networks as the baseband signaling can transmit the digital signal for a short distance only. And there is a requirement of repeaters for transmitting the signals. | Broadband transmission is mostly used for telephone networks. The broadband signaling can transmit the analog signals for long-distance without using any external device like a repeater or attenuator. |

## Modelo de referência OSI/ISO 
- Modelo em 7 camadas para interconexão entre sistemas abertos (solução pública, aberta)
- Modelo complexo, muito bloated porque foi elaborado por muitas pessoas.


**TCP é um modelo simplificado do modelo OSI (Universidade de berkley - USA)**

**Protocolo de rede é casado com tudo, bancos, computador, roteador, OS, etc ...**

- Cabeçalhos servem para fazer o dialogo com a entidade parceira do outro lado no mesmo nível.

>You need to address Open System Interconnect (OSI) Layer 1, the Physical layer, to resolve the problem. IP-based video conferencing applications are bandwidthintensive and may cause the network to slow down unless there is enough bandwidth to ensure proper network operation. To resolve bandwidth problems, you may need to switch to a higher capacity network backbone, which may require a change of cabling or media types, such as fiber optics. Cabling and network media types are defined at OSI Layer 1. The seven layers of the OSI model are as follows, in descending order from Layer 7 to Layer 1: 
>
>  **7. Application**: Interacts directly with the application. It provides application services, such as e-mail and File Transfer Protocol (FTP). 
>  **6. Presentation**: Enables coding and conversion functions for application layer data. The Presentation layer converts data into a format that is acceptable by the application layer. The formatting and encryption of data is done at this layer. 
>  **5. Session**: Creates, manages, and terminates sessions between communicating nodes. The session layer handles the service requests and responses that take place between different hosts. 
>  **4. Transport**: Delivers data sequentially and without errors. This layer manages data transmission between devices, a process known as flow control. The Transport layer protocols are Transmission Control Protocol (TCP) and User Datagram Protocol (UDP).
>  **3. Network:** Defines the network address or the Internet Protocol (IP) address, which is then used by the routers to forward the packets. 
>  **2. Data Link**: Ensures the reliable delivery of data to the physical address of the destination. include fiber optic, wireless, and Ethernet. ciscoexam.online
>  **1. Physical Layer**: Ensures the passage of data via phisycal means such as wire or wireless methods 

### Software Orientado a conexão e software não orientado a conexão

#### Obs: 
- Se N é OC (Orientada a conexão). 1. Connect (req/ind, resp/conf); 2. data. req/ind; 3. Disconnect (req/ind)
- Se N é NOC (Não orientada a conexão). Data. req/ind.

## Hubs, Switches, Routers
- Hubs: receive and distribute the packets into all the nodes of the network, even those that were not intended to receive them (dum)
- Switches: receive and distribute the packets on specific node of the network, through its MAC adress (smart)
- Routers: connect networks, fowarding the frames through IP adress (smart)

> ARP: protocol for mapping an IP adress to a MAC adress on a LAN
> Has an ARP table with cached dynamic IP -> MAC that it gets via broadcast and static ones that are added mannually

> MAC is used to comunicate in the same network
> IP is used to comunicate nods between different networks

## IP adress
- IPv4: 4 bytes/ 32 bits address ( four octates - 00000000.00000000.00000000.00000000 in decimal it is represented by 4 numbers in-between '.' ranging 0 to 255)

	  ![[TableOfIPv4.png]]

> Its important to remember that the first adress and the last one are reserved for network and broadcast respectively. So the true range of the first on would be 1-126

- IPv6: 16 bytes/ 128 bits adress ( 2001:0BAA:0000:0000:0000:24D2:12AB:98BC . Oito grupos, com quatro símbolos hexadecimais separados por dois pontos ( : ) )

### Subnetting
- Subnetting table
![[subnetting-table.png]]

- Example
![[example-subnetting.png]]

