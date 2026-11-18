# Laboratório de autenticação: Kali Linux, Medusa, Metasploitable e DVWA

Projeto de estudo em texto sobre riscos de autenticação e defesa em ambientes de laboratório. O objetivo é documentar os cenários e as medidas preventivas, sem executar tentativas de acesso.

## Escopo

O estudo considera três tipos de cenário:

- **FTP:** tentativas repetidas de autenticação contra um serviço vulnerável.
- **Formulário web (DVWA):** tentativas automatizadas de login.
- **SMB:** tentativas distribuídas entre contas e risco de enumeração de usuários.

Medusa é citada como ferramenta de auditoria de autenticação, e Metasploitable/DVWA como ambientes vulneráveis de treinamento. Este repositório **não contém comandos operacionais, wordlists ou automação de login**. Os exemplos de código abaixo analisam somente eventos fictícios em arquivo; não se conectam a serviços e não validam acessos.

## Ambiente seguro

Se você montar um laboratório por conta própria, utilize somente VMs descartáveis em rede virtual interna/host-only, sem exposição à Internet ou a redes de terceiros. Use contas e senhas fictícias, e confirme que os serviços não estão acessíveis fora do laboratório. A autorização deve ser explícita e limitada aos sistemas que você controla.

## Observações esperadas em uma avaliação defensiva

- **FTP:** repetidas falhas de autenticação podem indicar tentativa automatizada. Registre origem, horário e resultado; prefira SFTP/SSH e desative FTP simples quando possível.
- **DVWA:** picos de falhas no formulário devem ser correlacionados com os logs da aplicação e do servidor. Use MFA quando aplicável, limitação de taxa e monitoramento contra automação abusiva.
- **SMB:** tentativas contra várias contas podem escapar de alertas que observam apenas uma conta. Correlacione origem e sequência temporal; restrinja SMB por segmentação e desative SMBv1.

Como não foram feitas tentativas, não há credenciais ou acessos a validar. Em um relatório autorizado, documente apenas resultados obtidos no próprio laboratório, sem publicar senhas ou dados pessoais.

## Demonstração offline

O arquivo `examples/auth_events.csv` contém eventos inventados para FTP, web e SMB. Para gerar um resumo local, execute a partir da pasta do repositório:

```bash
python examples/analyze_auth_logs.py
```

O script conta falhas por serviço e origem, sinaliza três ou mais falhas e destaca um sucesso ocorrido depois de falhas daquela origem/serviço. A contagem cobre o arquivo inteiro: é uma demonstração simples, não um detector de produção nem uma análise temporal. Os endereços `192.0.2.x` são reservados para documentação.

## Mitigações recomendadas

1. Habilitar MFA, sobretudo para acesso remoto e contas administrativas.
2. Usar senhas únicas e longas e impedir senhas comuns ou comprometidas.
3. Aplicar limites de tentativas e atrasos progressivos sem facilitar bloqueios maliciosos de contas.
4. Centralizar e revisar logs de autenticação; alertar para falhas repetidas e sucessos incomuns.
5. Restringir serviços por firewall e segmentação, aplicar atualizações e remover contas desnecessárias.
6. Definir um procedimento para preservar logs, investigar alertas e revogar credenciais comprometidas.

## Conclusão

Ferramentas de auditoria ajudam a compreender riscos, mas devem ser utilizadas apenas com autorização. A entrega é intencionalmente simples: documentação, recomendações defensivas e um analisador offline de eventos fictícios, sem execução de ataques.
