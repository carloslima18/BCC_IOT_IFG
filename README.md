# BCC_IOT_IFG

Repositório para códigos desenvolvidos na aula de IOT do IFG Anápolis - Bacharelado em Ciência da Computação - 2019/2

## Getting Started

Para executar tarefas permanentemente, adicione a chamada a função em um sh dentro de um laço de repetição com condição sempre verdadeira:  https://github.com/Tadayuki123/BCC_IOT_IFG/blob/master/start_command.sh

E para chamar a função na inicialização do sistema:

```
sudo chmod +x /etc/rc.local
sudo vi /etc/rc.local
```
& adicione a chamada ao código ao fim do arquivo rc.local
```
sh /root/start_bengala.sh
```


## Related

* [Raspberry Pi](https://www.raspberrypi.org/) 
