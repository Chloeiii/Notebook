##  [What Is SSL/TLS](https://www.acunetix.com/blog/articles/tls-security-what-is-tls-ssl-part-1/) :cat:

POSTED ON  [APRIL 3, 2019](https://www.acunetix.com/blog/articles/tls-security-what-is-tls-ssl-part-1/ "7:30 am") BY  [AGATHOKLIS PRODROMOU](https://www.acunetix.com/blog/author/aprodromou/ "View all posts by Agathoklis Prodromou")  

Secure Sockets Layer (SSL) and Transport Layer Security (TLS) are cryptographic security protocols. They are used to make sure that network communication is secure. Their main goals are to provide data integrity and communication privacy. The SSL protocol was the first protocol designed for this purpose and TLS is its successor. SSL is now considered obsolete and insecure (even its latest version), so modern browsers such as Chrome or Firefox use TLS instead.

SSL and TLS are commonly used by web browsers to protect connections between web applications and web servers. Many other TCP-based protocols use TLS/SSL as well, including email (SMTP/POP3), instant messaging (XMPP), FTP, VoIP, VPN, and others. Typically, when a service uses a secure connection the letter S is appended to the protocol name, for example, HTTP**S**, SMTP**S**, FTP**S**, SIP**S**. In most cases, SSL/TLS implementations are based on the OpenSSL library.

SSL and TLS are frameworks that use a lot of  [different cryptographic algorithms](https://www.acunetix.com/blog/articles/tls-ssl-cipher-hardening/), for example, RSA and various Diffie–Hellman algorithms. The parties agree on which algorithm to use during initial communication. The latest TLS version (TLS 1.3) is specified in the IETF (Internet Engineering Task Force) document  [RFC 8446](https://tools.ietf.org/html/rfc8446)  and the latest SSL version (SSL 3.0) is specified in the IETF document  [RFC 6101](https://tools.ietf.org/html/rfc6101).

### Privacy & Integrity

SSL/TLS protocols allow the connection between two mediums (client-server) to be encrypted. Encryption lets you make sure that no third party is able to read the data or tamper with it. Unencrypted communication can expose sensitive data such as user names, passwords, credit card numbers, and more. If we use an unencrypted connection and a third party intercepts our connection with the server, they can see all information exchanged in plain text. For example, if we access the website administration panel without SSL, and an attacker is sniffing local network traffic, they see the following information.

![TLS Security ](https://www.acunetix.com/wp-content/uploads/2017/01/image32.png)  
The cookie that we use to authenticate on our website is sent in plain text and anyone who intercepts the connection can see it. The attacker can use this information to log into our website administration panel. From then on, the attacker’s options expand dramatically. However, if we access our website using SSL/TLS, the attacker who is sniffing traffic sees something quite different.

![TLS/SSL ](https://www.acunetix.com/wp-content/uploads/2017/01/image04-1.png)

In this case, the information is useless to the attacker.

### Identification

SSL/TLS protocols use public-key cryptography. Except for encryption, this technology is also used to authenticate communicating parties. This means, that one or both parties know exactly who they are communicating with. This is crucial for such applications as online transactions because must be sure that we are transferring money to the person or company who are who they claim to be.

When a secure connection is established, the server sends its SSL/TSL certificate to the client. The certificate is then checked by the client against a trusted Certificate Authority, validating the server’s identity. Such a certificate cannot be falsified, so the client may be one hundred percent sure that they are communicating with the right server.

### Perfect Forward Secrecy

Perfect forward secrecy (PFS) is a mechanism that is used to protect the client if the private key of the server is compromised. Thanks to PFS, the attacker is not able to decrypt any previous TLS communications. To ensure perfect forward secrecy, we use new keys for every session. These keys are valid only as long as the session is active.

## [ A Brief History of SSL/TLS](https://www.acunetix.com/blog/articles/history-of-tls-ssl-part-2/):dog:

 POSTED ON  [MARCH 31, 2019](https://www.acunetix.com/blog/articles/history-of-tls-ssl-part-2/ "7:42 am") BY  [AGATHOKLIS PRODROMOU](https://www.acunetix.com/blog/author/aprodromou/ "View all posts by Agathoklis Prodromou")

The Secure Sockets Layer (SSL) protocol was first introduced by Netscape in 1994. The Internet was growing and there was a need for transport security for web browsers and for various TCP protocols. Version 1.0 of SSL was never released because it had serious security flaws. The first official release of SSL, version 2.0, was out in 1995. The final version of the SSL protocol, SSL 3.0, was released in November 1996.

In 2011, the Internet Engineering Task Force (IETF) announced that SSL version 2.0 is deprecated. IETF recommended SSL v2 to be completely abandoned because according to a document that they released ([RFC 6176](https://tools.ietf.org/html/rfc6176)) the protocol has several major deficiencies. These included using MD5 for message authentication, lack of protection for handshakes, using the same key for message integrity and encryption, and easy session termination. In June 2015, IETF also announced that SSL 3.0 is deprecated. As stated in a document released by IETF ([RFC 7568](https://tools.ietf.org/html/rfc7568)), any TLS version is more secure than all versions of SSL. SSL also cannot use features of the TLS protocol such as Authenticated Encryption with Additional Data (AEAD), Elliptic Curve Diffie-Hellman (ECDH) and Elliptic Curve Digital Signature Algorithm (ECDSA), stateless session tickets, a datagram mode of operation (DTLS) and application-layer protocol negotiation.

## TLS to the Rescue

The Transport Layer Security (TLS) protocol was first introduced in 1999 as an upgrade to SSL v3. The TLS 1.0 RFC document ([RFC 2246](https://tools.ietf.org/html/rfc2246)) document states that  _the differences between TLS 1.0 and SSL 3.0 are not dramatic, but they are significant enough to preclude interoperability_. TLS 1.1 ([RFC 4346](https://tools.ietf.org/html/rfc4346)) was a minor update to TLS 1.0 released in April 2006. Some of the differences in this version included protections against Cipher Block Chaining (CBC) attacks. TLS 1.2 ([RFC 5246](https://tools.ietf.org/html/rfc5246)) was released in August 2008. Changes included adding cipher-suite-specified pseudorandom functions (PRFs), adding AES cipher suites, removing IDEA and DES cipher suites, and several other enhancements.

The current version of TLS, TLS 1.3, was released in August 2018 ([RFC 8446](https://tools.ietf.org/html/rfc8446)). It took IETF 10 years and 28 drafts to complete. This time, the protocol underwent some major changes with the focus on simplicity. Several unsafe technologies were removed, including SHA-1, MD5, RC4, DES, and 3DES. The protocol was streamlined for better performance: the handshake now requires only one round-trip (in some cases even zero). Other changes include encryption of SNI information for better privacy and a new signature standard (RSA-PSS). All modern browsers support TLS v1.3.
