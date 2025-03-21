

# Security and Privacy of QR Code Applications: A Comprehensive Study, General Guidelines and Solutions

# Heider A. M. Wahsheh 1,2 and Flaminia L. Luccio 1,∗

1 DAIS, Università Ca’ Foscari Venezia, 30172 Venezia, Italy; heider.wahsheh@unive.it

2 College of Computer Sciences and Information Technology, King Faisal University, Al-Hassa 31982, Saudi Arabia

* Correspondence: luccio@unive.it; Tel.: +39-041-2348448

Received: 2 March 2020; Accepted: 14 April 2020; Published: 16 April 2020

# Abstract

The widespread use of smartphones is boosting the market take-up of dedicated applications and among them, barcode scanning applications. Several barcodes scanners are available but show security and privacy weaknesses. In this paper, we provide a comprehensive security and privacy analysis of 100 barcode scanner applications. According to our analysis, there are some apps that provide security services including checking URLs and adopting cryptographic solutions, and other apps that guarantee user privacy by supporting least privilege permission lists. However, there are also apps that deceive the users by providing security and privacy protections that are weaker than what is claimed. We analyzed 100 barcode scanner applications and we categorized them based on the real security features they provide, or on their popularity. From the analysis, we extracted a set of recommendations that developers should follow in order to build usable, secure and privacy-friendly barcode scanning applications. Based on them, we also implemented BarSec Droid, a proof of concept Android application for barcode scanning. We then conducted a user experience test on our app and we compared it with DroidLa, the most popular/secure QR code reader app. The results show that our app has nice features, such as ease of use, provides security trust, is effective and efficient.

# Keywords

QR codes; barcode scanners; Android security; QR code security; QR code privacy

# 1. Introduction

Barcodes are a universal technology that provides visual data representation using series of lines, squares or dots, organized in a standard way. The barcode image contains information that identifies and describes the object it is associated to. In order to extract the encoded data, the user needs a barcode scanner, i.e., an optical machine that has imaging and processing capabilities (a camera and a processor). The barcode scanners can be specific devices or smartphone reader applications, and they require a Line-of-Sight to capture the barcode image and retrieve the stored data [1].

Two dimensional (2D) barcodes are machine readable images that enhance many features of the traditional one dimensional (1D) barcodes, such as more data capacity and robustness, and so are suitable for industrial and economic purposes. They can be used in a simple and effective way to achieve communication between physical objects (such as paper-based surfaces), and the digital ones (e.g., smartphones) [2].

Quick Response (QR) codes are particular 2D barcodes that have spread dramatically over the last few years, and they are considered free, simple and effective tools capable to store up to 2953 bytes that can be retrieved quickly [3]. Recently, new types of QR codes have been proposed that have a

Information 2020, 11, 217; doi:10.3390/info11040217 www.mdpi.com/journal/information

Information 2020, 11, 217

beautified appearance and a higher capacity [4]. QR codes allow users to extract data in three main modes: online, offline or in a combination of modes. For example, users can use QR codes to connect to websites, to send emails or read SMS, to save contact numbers, find map coordinates, listen to audio, or watch videos, etc. [5].

Recent studies show that barcodes can be maliciously used to run different attacks such as: phishing, malware propagation, cross-site scripting (XSS), SQL/command injection and reader applications attacks (see, e.g., [6]). Several QR code reader applications claim to provide security and privacy characteristics. In our opinion, it is important to categorize, evaluate and discuss the feature of these applications. In this study, we thus analyse 100 barcode scanner applications from a security and privacy perspective. According to our analysis, there are some apps that provide security services including URL checking and cryptographic solutions. Other apps guarantee user privacy by adopting least privilege permission lists. However, there are also apps that deceive the users by providing security and privacy protections which are weaker than what is claimed. We also analyze the most popular downloaded apps, since being popular does not imply being secure. Based on that, we classify the apps into five groups: URL Security, Crypto-based security, Popular, Save privacy, Weak applications. We recommend a set of tips for developers to build usable, secure and privacy-friendly applications and we used them to implement BarSec Droid, a proof of concept Android application for barcode scanning. Finally, we have conducted different experiments to evaluate user experience on our app compared to DroidLa, the most popular/secure QR code reader [7]. The results show that applying the design tips will increase the user security trust, improve the user attitude towards applying security solutions, and increase the awareness of possible attacks. This paper is an extended version of [8].

# 1.1. Contributions

Our contributions can be summarized as follows: (i) we present the most comprehensive analysis of 100 barcode scanner applications from security and privacy perspectives; (ii) we categorize barcode scanner applications into five groups based on the security features they provide or on their popularity; (iii) we propose usability, security and privacy recommendations for the development of barcode scanners; (iv) we present BarSec Droid, a proof of concept QR code Android application that we have developed; (v) we present the results of a user experience test on BarSec Droid and on DroidLa the most popular/secure QR code reader, and we discuss the comparison results.

# 1.2. Related Work

In the literature, there are some works that analyze QR code scanner applications, however, they take into consideration only a very limited number of them. To the best of our knowledge, our work contains the most comprehensive analysis of security and usability features of QR code readers (we have studied 100 applications).

In [9], the authors investigate the security features of 31 Android QR code scanner apps, w.r.t. phishing and malware attacks. Twenty-three out of 31 apps ask user permission before visiting the encoded QR code URLs. Only two QR code scanners, Norton Snap and QR Pal, provide some security warnings but have very poor detection capabilities of link-based phishing and malware attacks. Therefore, the authors propose SafeQR app which employs two security APIs, Google safe browsing and Phishtank [10,11] to enhance the detection rate of malicious URLs. However, w.r.t. our work, the study of [9] does not discuss the usability and privacy properties, and does not provide solutions for other attacks such as, e.g., SQL and command injections.

The study of [12] focuses on QR code security, usability and privacy issues. The authors initially study the 12 most frequently used QR code reader applications for Android, iOS and Windows Phone, w.r.t. security protection and privacy violations. The results show the inefficiency of protection methods against malicious QR codes and the lack of privacy protection (sensitive data were sent to third parties). In the second part of the work, the authors assess user knowledge about QR code.

Information 2020, 11, 217 3 of 23

security by using an online questionnaire. The results show differences between users of different European countries, and also underline the need of security improvements in the QR code processing phase. Finally, the authors propose a set of design recommendations to improve usability and security of QR code scanners. The authors present a prototype that checks the online content and adopts digital signatures, and the results show the efficiency of the protection recommendations. W.r.t. to our work, the study of [12] analyzes only a small number of applications and does not consider the expected size or delay overhead of applying digital signature mechanisms.

The study of [13] focuses on 14 Android QR code scanners, explores their security proprieties, and shows limited capabilities and weaknesses of several apps from a protection point of view. In particular, some apps directly visit the URL encoded in the barcorde, neither validating it against threat databases, nor asking user’s permission, thus putting users at a risk of being redirected to malicious websites. Only two apps, KasperSky [14] and G Data QR code [15] perform validation of the full URL, and only 8 out of 14 analyzed apps provide security features against phishing and malware attacks. Finally, the author gives some tips on how to enhance the protection of barcode readers, but, w.r.t. our work, does not analyze them from a usability perspective.

# 1.3. Paper Structure

The rest of this paper is organized as follows: Section 2 introduces our research methodology, while Section 3 presents QR code reader applications and categorize them based according to their properties. In Section 4, we evaluate all tested barcode reader applications in terms of granted permissions. In Section 5, we first illustrate our recommendations for the development of secure, usable and privacy-friendly QR code readers, and we then present BarSec Droid, our implemented reader application. Section 6 shows a user experience test on our app, and finally, in Section 7 we present the conclusion and future work.

# 2. Research Methodology

In this section, we present the research methodology that we used, and we emphasize the differences with our previous work [8]. Our methodology includes the following six main steps:

1. Application selection: We have searched inside Google Play Store for Android secure and privacy-friendly barcode reader applications and we have selected 100 of them. This extends the work of [8] where we only considered 28 apps.
2. Information gathering: We have extracted all the features and permissions from the app descriptions.
3. Application tests: We have installed the apps, evaluated them and compared their capabilities w.r.t. the app descriptions.
4. Application Categorization: According to the app features, we have divided them into five different groups, refining the categorization of [8];
5. Recommendation proposal: We have listed guidance tips for developers to build secure and privacy-friendly barcode reader apps;
6. User security and usability awareness evaluation: We have conducted a user survey to evaluate the user experience. This survey extends the one of [8], as it was refined and the number of proposed questions was increased.

# 3. QR Code Readers

Exploring Google Play Store [16] for secure QR code readers lead to a selection of more than 100 apps. All these apps support the standard scanning service but some of them also claim to provide security features. According to [12] most barcode scanners apps are not able to protect users against the selection of malicious QR codes, or against privacy violations. In this study, we aim at studying barcode reader applications from security, privacy and usability perspectives. Our preliminary results in [8] showed that several apps use weak security mechanisms, e.g., weak algorithms or short key lengths. Moreover, several apps do not follow standard structures or optimal encoding schemes.

Our proposed app, in Section 5 overcomes all these limitations. Table 1 lists the following features of the selected apps:

- App developer: the identity of developer or company name.
- Version: analyzed app version.
- Installs: number of app installations from Google Play.
- Category: App’s category (w.r.t. later classification).
- Rate: a 5-point scale users evaluation of an app from Google Play. N/A means not available.
- 1D/2D: ability to read 1D and 2D barcodes. QR stays for QR codes.
- Format: the reader displays the barcode type it has identified, e.g., QR code, etc.

# Table 1. Details of the Tested QR Code Readers.

|App Developer|Version|Installs|Category|Rate|1D/2D|Format|
|---|---|---|---|---|---|---|
|[7]|7.0.4|5 M+|Crypto and Popular|4.2|X| |
|[14]|1.2.4.51|1 M+|URL and Popular|4.4|QR| |
|[15]|1.0.2.0643c6ef|10 K+|URL|3.3|QR| |
|[17]|2.0.0.71|1 M+|URL and Popular|4.2|X| |
|[18]|1.0.0|10 K+|URL|4.8|X| |
|[19]|1.1|10+|URL|5|X| |
|[20]|1.2|100+|Crypto|5|X| |
|[21]|1.0.17|1 K+|URL|4.1|X|a|
|[22]|1.0|5 K+|URL|4.4|X|X|
|[23]|Freeb|100+|Crypto|5|QR| |
|[24]|2.5.0|100 K+|URL|4.3|X|X|
|[25]|1.0.0|100 K+|URL|4.3|QR| |
|[26]|1.6.1|10 K+|Save-Privacy|4.4|X|X|
|[27]|2.4.3|500 +|URL|4.1|X| |
|[28]|1.1|5 +|URL and Save-Privacy| |X| |
|[29]|1.03|500 K+|Weak|3.8|X|X|
|[30]|1.1.7|10 K+|Save-Privacy|4.2|X| |
|[31]|2.1.6|5 M+|Popular and Weak|4.5|X| |
|[32]|1.3.1-L|1 M+|URL, Popular and Save-Privacy|4.6|X|X|
|[33]|1.0.2|1 +|Crypto| |X| |
|[34]|1.7.6|10 M+|Save-Privacy and Popular|4.7|X| |
|[35]|2.33|50 M+|Popular and Weak|4|X| |
|[36]|Varies with device|100 M+|Popular|4.1|X|X|
|[37]|1.2.91|10 M+|Popular|4.6|X|X|
|[38]|Varies with device|50 M+|Popular and Save-Privacy|4.4|X| |
|[39]|1.25|5 M+|Popular|4.4|X|X|
|[40]|0.92|10 M+|Popular|4.6|X| |
|[41]|1.0.5|1 K+|Crypto|5|X| |
|[42]|1.0.12|500 K+|Weak|4.4|X| |

# Information 2020, 11, 217

# Table 1. Cont.

|App Developer|Version|Installs|Category|Rate|1D/2D|Format|
|---|---|---|---|---|---|---|
|[43]|1.1.5|1 K+|URL|4.4|X|Xc|
|[44]|2.2.18|10 K+|URL|4.2|X|Xc|
|[45]|3.0.8|50 M+|Popular|4.5|X| |
|[46]|2.0.3|100 K+|Weak|4.7|X|X|
|[47]|2.0|1 M+|Weak|4.0|X| |
|[48]|1.38|5 M+|Popular and Weak|4.3|X|X|
|[49]|1.1|1 M+|URL and Popular|4.6|X| |
|[50]|1.1.24|100 K+|Weak|4.3|X| |
|[51]|1.17|1 M+|Popular and Weak|4.7|X| |
|[52]|3.4|10 +|Save-Privacy|N/A|X|a|
|[53]|1.9.4|10 M+|Popular|3.8|X| |
|[54]|1.0|100 K+|Weak|4.6|X| |
|[55]|1.0|100 +|Weak|4.5|X| |
|[56]|1.0|1 K+|Weak|4|X|Xd|
|[57]|6.0.0|500 K+|Weak|4.6|X| |
|[58]|1.0.1|10 +|Save-Privacy|5|X|X|
|[59]|1.14-lite|10 K+|Weak|4.3|X| |
|[60]|1.3|1 +|Weak|N/A|X| |
|[61]|1.0|0 +|Weak|N/A|QR| |
|[62]|1.1|100 +|Weak|5|X| |
|[63]|1.0.1|1 +|Weak|N/A|X| |
|[64]|1.2|10 +|Save-Privacy|5|X| |
|[65]|1.0.4|10 K+|Weak| |X| |
|[66]|1.4.4|5 K+|Weak|4.6|X| |
|[67]|1.6|10 K+|Weak|4.2|X| |
|[68]|1.0|100 +|Weak|3.7|X|Xd|
|[69]|1.0|10 +|Save-Privacy|5|QR| |
|[70]|1.2.6|1 M+|Popular and Weak|3.9|X| |
|[71]|1.0.14|10 K+|Save-Privacy|4.7|X| |
|[72]|1.0.1|10 K+|Weak|3|X| |
|[73]|1.0|10 +|Save-Privacy|5|X| |
|[74]|2.0.0|500 +|Weak|N/A|X| |
|[75]|1.0.3.18|100+|Save-Privacy|4.2|X| |
|[76]|1.0|10 +|Weak|N/A|X| |
|[77]|1.0|5 +|Save-Privacy|N/A|X| |
|[78]|1.2|10+|Crypto|N/A|QR| |
|[79]|1.0|10 +|Crypto|N/A|QR| |
|[80]|1.10.3010|5 M+|Popular and Weak|4.7|X| |
|[81]|2.0.0|5 +|Crypto|5|X| |
|[82]|1.3|1 K+|Weak|4.9|X|X|
|[83]|2.0.2|50 +|Crypto and Save-Privacy|5|X|a|

# Table 1. Cont.

|App Developer|Version|Installs|Category|Rate|1D/2D|Format|
|---|---|---|---|---|---|---|
|[84]|1.2.1|10 K+|Weak|4.5|X| |
|[85]|1.0.1|10 +|Save-Privacy|N/A|X| |
|[86]|1.0.4|100 K+|Save-Privacy|4|X| |
|[87]|1.0|10 +|Save-Privacy|N/A|X| |
|[88]|1.0.8|1 M+|Popular and Weak|4.5|X| |
|[89]|1.1.0|10 K+|Weak|2.9|X| |
|[90]|1.1.5|50 K+|Weak|4.6|X|X|
|[91]|1.2.0.2|500 +|Save-Privacy|3.3|X| |
|[92]|1.0|10 +|Save-Privacy|5|X| |
|[93]|1.3|1 K+|Weak|3.5|X|X|
|[94]|1.4.15|50 K+|Weak|4.1|X| |
|[95]|1.0|5 K+|Weak|N/A|QR| |
|[96]|1.0|5 K+|Weak|3.6|X| |
|[97]|3.0|50+|Weak|5|X| |
|[98]|1.0.5|500+|Weak|4.1|X| |
|[99]|3.0|10 K+|Save-Privacy|4.3|X| |
|[100]|1.01|100 K+|Weak|4.3|X| |
|[101]|1.4.12|10 K+|Weak|4.6|X| |
|[102]|1.0|5 K+|Weak|2.5|X| |
|[103]|1.0|50+|Weak|N/A|X|X|
|[104]|1.0|1 K+|Save-Privacy|4.8|QR| |
|[105]|1.0.1|100+|Weak|4.5|X| |
|[106]|1.0.7|1 M+|Save-Privacy and Popular|4.6|X| |
|[107]|1.0.9|1 K+|Weak|4.8|X| |
|[108]|1.0|1 +|Save-Privacy|N/A|X| |
|[109]|1.0.4|5 +|Weak|N/A|QR| |
|[110]|1.0|10 +|Weak|5|X|X|
|[111]|1.0.4|10 K+|Weak|4.6|X| |
|[112]|1.2|50 +|Save-Privacy|N/A|X| |
|[113]|1.0|1 +|Weak|5|X| |

a Always displays QR code; b Free version to test functionality; c Displays barcode image; d Two buttons to read 1D barcode or QR code.

# 3.1. URL Security Applications

Embedding barcodes with malicious links is one of the most common attacks that targets a user device. In this section, we presents QR code readers that provide security services on links, by checking the encoded online content. Multiple technologies can be used for detecting malicious URLs, e.g., Artificial Intelligence techniques, black and white lists, etc., however, in this context, we do not focus on the adopted technology but on the features provided by the readers.

G Data QR code reader [15] is a free Android application that checks the online content of a QR code, detects suspicious links, shows the complete URL and extends short ones, and blocks users from visiting unsafe URLs in their browser [13].

Information 2020, 11, 217 7 of 23

KasperSky QR Scanner [14] is a free app that checks QR code URLs against malicious Web pages. The app description does not provide any detail regarding the used protection methods, and the main limitation of the app is that it allows to directly visits links, detected as benign, without asking for user confirmation [13].

The Norton Snap QR code scanner [17] is another application that validates QR code URLs against Web attacks. This app alerts users for benign/malicious links, blocks malicious URLs, and retrieves the full encoded URL.

Other URL security applications such as: Trend Micro [18], FANSec [19], Dennings [21], Avira [24], iTechSo [28], KidControl [22], iTechSol [28,49] and X & C Hi-Tech Inc. [27] provide URL checking services. However, they do not retrieve the full URLs. If the encoded URLs are shortened or redirected, the users will not be able to check the final URL destination.

QR Code Scanner & Barcode Reader for CM Browser [25] is a lightweight QR code scanner based on the CM browser: it is the browser itself that provides security services, checks URLs, and blocks advertisements.

TeaCapps barcode scanner [32] checks URLs by employing Chrome Custom Tabs, which uses Google Safe Browsing technology [10].

G-Scan and G-tos scan barcode scanners [43, 44] check URLs, alert users in case of malicious links and gets the full expanded URLs.

# Table 2. Barcode Scanners that check URLs contained Inside QR codes.

|App Developer|Check URL|Display URL|Get Full URL|Direct Open|URL Checking Technique|
|---|---|---|---|---|---|
|[14]|X| | |Xa|KasperSky Virusdesk|
|[15]|X|X|X| |N/A|
|[17]|X|X|X|Xa|Norton Safe Web|
|[18]|X|X| | |N/A|
|[19]|X|X| | |N/A|
|[21]|X|X| | |Google Safe Browsing|
|[22]|X|X| | |N/A|
|[24]|X|X| | |N/A|
|[25]|X| | |X|CM browser|
|[27]|X| | |Xa|N/A|
|[28]|X|X| | |N/A|
|[32]|X|X| | |Google Safe Browsing|
|[43]|X|X|X| |N/A|
|[44]|X|X|X| |N/A|
|[49]|X|X| | |N/A|

a Directly opens the URL if it is safe. N/A means not available.

The main limitation of these apps is that URL-checking scanners works against online attacks, by detecting malicious/suspected Web pages, while other offline attacks such as SQL and command injections cannot be prevented. Moreover, some of these applications do not provide information about their URLs checking techniques, i.e., how they classify URLs into benign or malicious.

# 3.2. Crypto-Based Security Applications

Cryptographic mechanisms can be used to encrypt, sign and control the access to QR code content. Adopting data encryption provides confidentiality and access control for the encoded contents, so that

only the authorized users (who have the decryption key) can retrieve the encoded data. Moreover, digital signatures can achieve authentication, integrity and non-repudiation. Recent studies also investigate the use of Visual Secret Sharing schemes for QR Code, to provide additional security mechanisms, e.g., to online transaction [ 114 ]. Choosing the suitable algorithm, key length and structure are discussed in multiple studies [ 6 ,115 ], but the key factor on barcode usability is the size overhead [ 116 ]. However, there are few applications that offer generating and reading cryptographic QR codes.

Madiff Net reader application [ 20 ] is free and available in several languages, such as: English, Vietnamese and Chinese. Madiff Net supports scanning and generating password-protected QR codes, in which the content is encrypted using a shared key between the generator and the barcode reader. The developer does not mention the used algorithm but keys are 6 bytes of length, and the ciphertext is a base 64 string. Since the algorithm is unknown, we cannot evaluate the strength of this app. In addition, Madiff Net uses a base 64 encoding scheme for bytes inside QR codes which causes size overhead.

QR Droid Private [7] is a free, well-designed interface, which provides scanning and QR code generation services. This app supports URL shortening, QR code sharing and content encryption. QR Droid Private adopts a weak encryption algorithm, i.e., Data Encryption Standard (DES) with breakable key size of 56 bits. It uses a keyword structure, in which the ciphertext is encoded in base 64. There are two versions, private and full. The private version needs few permissions to generate QR codes, while the full version needs more permissions.

Crypto Message [23] is a security application that supports an encryption service for encoding text messages inside QR codes. This application offers the creation of QR codes in the free version, while decoding requires the paid version. It adopts Advanced Encryption Standard (AES) with four modes that include: Electronic Codebook (ECB), Cipher Block Chaining (CBC), Counter (CTR), and Output Feedback (OFB) modes. It uses key size of 128, 192 and 256 bits, and encodes ciphertexts as hexadecimal or base 64 strings. Finally, Crypto Message is not able to decode barcodes that are created by other applications.

The algorithm, the key size and the structure of EC QR [33 ,41 , 78, 79, 81 ,83 ] are not available and cannot be evaluated. However, the developers claim they support message encryption and other security features.

Observe that, all the above mentioned applications have some limitations: (1) They assume no standard method of encoding cryptographic data in QR codes, i.e., each application adopts its own structure. Thus, in order to decode a crypto-barcode, the user will need to use the same generating application, while, on the other hand, the study of [ 116 ] suggests the use of the standard JavaScript Object Notation (JSON) as a general structure to be used with crypto-QR codes. (2) Some of these applications use weak encryption algorithms such as: DES and AES-ECB. (3) These applications employ base 64 and hexadecimal strings to represent ciphertexts, which lead to size overhead.

The password-protected QR codes achieve confidentiality and access control, so that only authorized users who have the key (password) can decrypt and access contents. However, encrypting the contents is not the optimal mechanism to protect users who scan the QR code, since even encrypted data may include malicious URLs or offline attacks. Digital Signature can be useful to protect users, as it employs public-key cryptography, to validate authentication, integrity and non-repudiation of QR code contents [116 ].

# Table 3

presents a summary of crypto-based QR code scanners and it includes the app developer, encryption, digital signature (DS), algorithm (Alg), key length (KL), encoding scheme (EncS), and structure (Str).

Note that, these applications offer a single access control mechanism, the encoded data may either be public (plain text) or private (ciphertext), thus they do not support QR codes that have an encrypted part and a plaintext at the same time. Moreover, none of the applications support digital signature.

# 3.3. Popular Applications

In this section, we explore the most popular QR code scanner applications that have been downloaded by more than 1 million users (see Figure 1). Note that, popular apps may be included in the other groups, for example Norton Snap [17] and KasperSky [14] are included in the URL security group, as well as in the Popular applications group (see Table 1).

# Table 3. Crypto-based QR Code Scanners.

|App Developer|Encryption|DS|Alg|KL (Bits)|EncS|Str|
|---|---|---|---|---|---|---|
|[7]|X|X|DES|56|Base64|Keyword|
|[20]|X|X|N/A|48|Base64|N/A|
|[23]|X|X|AES|128,192 & 256|Base64 & hex|N/A|
|[33]|X|X|N/A|N/A|Base64|N/A|
|[41]|X|X|N/A|N/A|Base64|N/A|
|[78]|X|X|N/A|N/A|Base64|N/A|
|[79]|X|X|N/A|a|Base64|N/A|
|[81]|X|X|N/A|N/A|Base64|N/A|
|[83]|X|X|N/A|N/A|Base64|N/A|

a Pin number (4 digits).

# Figure 1. Popular QR Code Scanners.

The ZXing library [117] (“zebra crossing”) is a Java source image processing library that is compatible with several 1D and 2D barcodes and used with various popular applications such as: ZXing Barcode Scanner [36], Barcode Scanner Pro (10M downloads) [37], and Barcode Scanner [39] (5M downloads).

Information 2020, 11, 217

ZXing Barcode Scanner [36] is one of the most popular downloaded applications, with more than 100 million users. It employs [117], shows the barcode format and offers extra information about embedded links such as: title and redirections.

Other applications that have nearly the same functionalities, and are able to read 1D and 2D barcodes are QR & Barcode Scanner by [35, 38, 45] that recorded more than 50M downloads. Moreover, free QR Scanners Bar Code Scanner & QR Code Reader [40, 53] recorded 10M downloads. Private version of [7, 31, 80], recorded more than 5 M downloads.

Note that, being popular is not enough to be usable and secure. So we have investigated the popular applications also from security perspective. [14, 17, 49] belong to URL and popular groups, while [34, 38, 106] belong to popular and Save-Privacy groups. [7] belongs to Crypto and Popular, and [32] belongs to three groups, i.e., URL, Popular and Save-Privacy. Moreover, we have also evaluated all tested apps from privacy perspectives (see Tables 4 and 5).

# 3.4. Save-Privacy Applications

Using a barcode reader application involves asking for user permissions, a list of allowed services and resources that the app can use, e.g., contacts, media files, camera or microphone. Granting these permissions allows the app to facilitate the barcode usage, e.g., saving a phone number directly without copy and paste. However, giving permissions can be extremely dangerous, especially from a privacy perspective, as an attacker may access private data and may run an information leakage attack. The problem of correctly configuring systems so to protect the user privacy is a very challenging task in general and has been widely studied also in other contexts, e.g., to correctly configure TLS/SSL connections in mobile applications [118], or to configure products and systems in the software industry [119]. In this section, we will illustrate the available apps that adopt balanced permissions that meet the privacy requirements. In the context of QR codes, we need standard architectural choices for developers to build privacy-friendly applications, with minimal permissions include accessing the camera (to scan the barcode), and the network (if there is a need to check URLs).

# Table 4: Save-Privacy Apps with Least-Privilege Permissions

|Permissions|Description|
|---|---|
|Camera (Cam)|takes pictures and videos|
|Wi-Fi info (wi-fi)|views Wi-Fi connections|
|Network (Net)|gives full network access, and views network connections|

TeaCapps Scanner [28, 32] are examples of apps that support checking QR code online contents, alongside with less permissions (camera and Internet). QR Scanner (Privacy Friendly) [26], Tokoware [85], Krow QR Code Reader [87], and Habib Khlifi QR Code Reader [108] are all QR code readers that only ask camera permission. If users are interested in privacy, these are the suitable application. They are safe and fully compatible with Android devices.

Tokoware [30], Lightning QR code Scanner [34, 52, 64, 69, 75, 83, 91, 92, 104, 112] require access to the camera and to the network. Thus, all these applications are suitable for users who aim at protecting their privacy.

Some other apps in Table 4 such as: [38, 58, 71, 73, 77, 99, 106] also ask for Wifi permission that should not violate the user privacy.

# Table 4. Save-Privacy Apps with the Least-Privilege Permissions.

|App|Developer|Camera|Network|Wi-Fi|
|---|---|---|---|---|
|[26]| |X| | |
|[28]| |X|X| |
|[30]| |X|X| |
|[32]| |X|X| |
|[34]| |X|X| |
|[38]| |X|X|X|
|[52]| |X|X| |
|[58]| |X|X|X|
|[64]| |X|X| |
|[69]| |X|X| |
|[71]| |X|X|X|
|[73]| |X|X|X|
|[75]| |X|X| |
|[77]| |X|X|X|
|[83]| |X|X| |
|[85]| |X| | |
|[86]| |X|X|X|
|[87]| |X| | |
|[91]| |X|X| |
|[92]| |X|X| |
|[99]| |X|X|X|
|[104]| |X|X| |
|[106]| |X|X|X|
|[108]| |X| | |
|[112]| |X|X| |

# 3.5. Weak Applications

In this section, we present apps that try to deceive the users by claiming strong security-privacy features, without providing any real protection. These apps employ misleading terms such as data encryption and decryption, while they do not provide real cryptographic mechanisms (False encryption) and refer to these terms to indicate data encoding and decoding in QR codes such as: [ 102 ,103 ,109 ]. Here it is important to mention that data encoding means representing data in QR code modules, where any QR code scanner can retrieve (decode) the contents directly without any specific key (see part (a) in Figure 2). On the other hand, data encryption means transforming data (plaintext) into an encrypted message (ciphertext), that only authorized users who have secret key can decrypt (see part (b) in Figure 2).

Information 2020, 11, 217 12 of 23

# Encode

Data Plain Text

Encrypt

Data Plain Text

Data Cipher Text

(b)

Figure 2. (a) Encoding data in QR Codes. (b) Encrypting and then encoding data in QR Codes.

Moreover, some apps’ descriptions indicate security and privacy features, while testing them shows that they do not really provide the claimed features such as [51,63,80,101,105,107,110,111]. Other apps claim they are privacy-friendly but ask for potential permissions that can be used in information leakage attacks, such as: [29,31,35,42,46–48,50,54–57,59–62,65–68,70,74,76,84,88–90,93–98,100,113]. More details will be given in the next section.

# 4. Permissions and Privacy Evaluation

Reviews on barcode applications generally show dissatisfaction when applications require unneeded permissions. As an example, we cite a user review of [35] application. A user wrote: “Why do you now need access to my location, photos, media and files? It worked perfectly in the past without these permissions and I see no reason to have them”. This comment shows how limiting permissions can be an important feature.

For this reason, we have decided to evaluate all the tested barcode reader applications in terms of granted permissions. Table 5 shows the requested permissions for all our 100 tested applications excluding the apps that we already analyzed in Table 4. These permissions include getting access to:

- Device & app history (DevHis): read sensitive log data;
- Contacts (Cont): read contacts;
- Location (Loc): approximate location (network-based) and precise location (GPS and network-based);
- Phone (Phn): directly call phone numbers;
- Photos/media/files (Files): read, modify or delete the contents of USB storage;
- Storage (Stg): read, modify or delete the content of USB storage;
- Device ID & call info (DevInf): read phone status and identity;

# Information 2020, 11, 217

# Table 5. Permissions of Tested QR Code Readers.

|App|Developer|DevHis|Cont|Loc|Phn|Files|Stg|Cam|Wi-Fi|DevInf|Net|
|---|---|---|---|---|---|---|---|---|---|---|---|
|[7]| |X|X|X| |X| | | | | |
|[14]| |X|X|X|X|X|X| | | | |
|[15]| |X| |X|X|X|X| | | | |
|[17]| |X|X|X|X| |X|X| | | |
|[18]| |X| |X|X|X|X| | | | |
|[19]| |X| |X|X|X|X|X|X|X| |
|[20]| |X|X|X|X|X|X|X|X|X| |
|[21]| | |X|X| |X|X| | | | |
|[22]| | |X|X| |X| | | | | |
|[23]| | |X| |X|X|X| | | | |
|[24]| |X|X|X|X|X|X|X|X|X| |
|[25]| | |X|X| |X|X|X| | | |
|[27]| | |X|X| |X|X|X|X|X| |
|[29]| | |X|X| |X|X|X|X|X| |
|[31]| | |X|X| |X|X|X|X|X| |
|[33]| | |X|X| |X|X| | | | |
|[35]| |X| |X|X|X|X|X|X|X| |
|[36]| |X|X| |X|X|X|X|X|X| |
|[37]| |X|X| |X|X|X|X|X|X| |
|[39]| |X|X| |X|X|X|X|X|X| |
|[40]| |X| |X|X|X|X| | | | |
|[41]| | |X|X| |X|X| | | | |
|[42]| | |X|X| |X| | | | | |
|[43]| | |X|X|X|X|X|X|X|X| |
|[44]| | |X|X|X|X|X|X|X|X| |
|[45]| | |X|X| |X|X|X|X|X| |
|[46]| | |X|X| |X|X|X|X|X| |
|[47]| | |X|X| |X|X|X|X|X| |
|[48]| |X| |X|X|X|X|X|X|X| |
|[49]| |X|X|X|X|X|X|X|X|X| |
|[50]| |X| |X|X|X|X|X|X|X| |
|[51]| | |X|X|X|X|X|X|X|X| |
|[53]| | |X|X|X|X|X|X|X|X| |
|[54]| | |X|X|X|X|X|X|X|X| |
|[55]| |X| |X|X|X|X|X|X|X| |
|[56]| |X| |X|X|X|X|X|X|X| |
|[57]| | |X|X| |X| | | | | |
|[59]| | | |X|X|X|X|X|X|X| |
|[60]| | | |X|X|X|X|X|X|X| |

# Table 5. Cont.

|App Developer|DevHis|Cont|Loc|Phn|Files|Stg|Cam|Wi-Fi|DevInf|Net|
|---|---|---|---|---|---|---|---|---|---|---|
|[61]| |X|X|X|X|X| |X| |X|
|[62]| |X|X|X| | |X| | |X|
|[63]| |X| |X|X|X| |X|X| |
|[65]| |X|X|X| | |X| | |X|
|[66]| |X|X|X|X|X| |X| |X|
|[67]| |X|X|X|X|X| |X| |X|
|[68]| |X| |X|X| | |X| | |
|[70]| |X|X|X|X| | |X| |X|
|[72]|X| |X|X|X|X|X|X| |X|
|[74]| |X|X|X|X|X|X| | |X|
|[76]|X| |X|X|X|X|X|X| |X|
|[78]| |X|X|X| | |X| | |X|
|[79]| |X|X|X|X| | |X| |X|
|[80]| |X|X|X|X|X|X| | |X|
|[81]| |X| |X|X|X| | | |X|
|[82]| |X|X|X| | |X| | |X|
|[84]| |X|X|X|X| | |X| |X|
|[88]| |X|X| |X|X|X| | |X|
|[89]|X| |X|X|X|X|X|X| |X|
|[90]| |X| |X|X|X|X|X| |X|
|[93]|X|X| |X|X|X| |X| |X|
|[94]|X| | |X|X|X| |X| |X|
|[95]| |X|X|X|X| | |X| |X|
|[96]| |X|X|X|X| | |X| |X|
|[97]| |X| |X|X|X| |X| |X|
|[98]| |X| |X|X| | |X| | |
|[100]| |X| |X|X| | |X| | |
|[101]| |X| |X|X| | |X| | |
|[102]| |X| |X|X| | |X| | |
|[103]| |X| |X|X| | |X| | |
|[105]| |X|X|X|X|X|X| | |X|
|[107]| |X| |X|X| | |X| | |
|[109]| |X| |X|X| | |X| | |
|[110]| |X| |X|X| | |X| | |
|[111]|X|X|X|X|X|X|X| | |X|
|[113]| |X|X|X|X| | |X| | |

# 5. Secure and Usable Barcode Reader Applications

In this section we first discuss possible design recommendation to develop secure and usable barcode reader applications, and we then present BarSec Droid, a new application that follows this guidelines and has good user feedbacks.

# 5.1. Design Recommendation

Based on our assessment for the existing 100 barcode scanners, on limits and drawbacks previously mentioned, and based on suggestions proposed in other works [116, 120] we recommend the following guidelines to develop secure, usable, and privacy-friendly barcode reader applications:

- Barcode type: Support several barcode types, that can be used in various contexts;
- Barcode format: Display the barcode format, in order to avoid wrong barcode type decoding;
- URL checking: Check URLs inside barcodes to detect malicious ones;
- Warnings: Use security warnings such as browser warnings against suspicious URLs;
- Digital signature: Apply digital signature services, to authenticate the barcode generator, guarantee data integrity and non-repudiation;
- Encrypted content: Adopt encrypted contents, to achieve confidentiality and access control;
- Limit permissions: Request least-privilege permissions, and prevent accessing private files to guarantee user privacy. Limit permissions to camera access (to scan the barcode image), and to Internet (to check URLs);
- Simple interface: Provide default basic functionalities with simple interface, so that non-expert users can easily use the app;
- Prevent code execution: Prevent the execution of any encoded codes or commands in user devices;
- Supporting material: Provide manuals and resources for users to learn how to use secure reader applications.

# 5.2. The BarSec Droid Application

According to the recommendations presented in Section 5.1, we have developed two applications: the BarSec desktop application and the BarSec Droid Android application (Available at: https://apkpure.com/it/barsec-droid/barcode_security.heider.bsr). These applications adopt symmetric and asymmetric cryptographic mechanisms to generate and read secure and usable barcodes, and make use of the ZXing library [117]. Figure 3 presents the BarSec Droid Android application.

The barcode generator is available only in the BarSec desktop application, and generates barcodes using the JSON structure, as proposed in [116]. It offers various security features that include: barcodes authentication, data integrity, access control, and confidentiality. It provides usability warning messages based on the usability guide presented in [121] and can be used for both generating and reading QR codes.

Both the BarSec Droid Android application and the BarSec desktop application support different digital signature algorithms i.e., RSA and Elliptic Curve Digital Signature Algorithm (ECDSA) with several key lengths, and use SHA-256 as hash function (see Figure 3). They support hash-based message authentication code (HMAC) with different key lengths. In addition, they use Advanced Encryption Standard (AES) with four modes; Cipher Block Chaining (CBC), Output Feedback (OFB), Cipher Feedback (CFB) and Galois/Counter Mode (GCM). These mechanisms have been studied in detail to meet the usability issues presented in [121]. We have also implemented Access Control Lists (ACLs) that allow the generator to have multiple layers of data; i.e., multiple users who have controlled access to data.

# Information 2020, 11, 217

# BarSec Droid

Crypto_Check: Secure

Barcode Type: QR_CODE

Error Correction: L

# HelloBarSec Droid

# QR Code Security App

Hide Security Details

# Security Summary

Barcode Format: QR_CODE

Signature Algorithm: RSA1024withSHA256

Confidentiality: not Used

Encryption Algorithm:

Barcode Contents Size: 629 Bytes

Barcode Data Structure: JSON

Authentication, Data Integrity and Non-Repudiation Test: Guaranteed

Signature Length: 128 Bytes

Certificate Length: 378 Bytes

Certificate: {"CERT" {TA": Ca\'

Figure 3. Screenshot of a BarSec Droid Android application.

# Example 1

As an example of use assume we have a QR code with the ACL that include these tags: public, student and teacher, where:

- Public tag: contains plain text data;
- Student tag: contains a ciphertext that is encrypted with the student key.
- Teacher tag: contains a ciphertext that is encrypted with the teacher key.

Each tag has authorized users who can access its contents, e.g., a student can read the public tag, and the student tag but not the teacher tag (since students do not have the teacher key).

# Table 6

summarizes the features of the BarSec Droid application. It uses the JSON structure, and it supports barcodes generated by the BarSec Droid Desktop application, and also barcodes that contain Access Control Lists (ACLs). It can read standard QR codes that do not include cryptographic data and that do not follow specific structures. It checks full URLs contained inside barcodes, and checks their online content using Norton Safe Web service [122].

# Information 2020, 11, 217

# Table 6. BarSec Droid Specification.

|Feature|Supported|Key Length (Bits)|
|---|---|---|
|Encryption|AESa|128–256|
| |ECDSA|256|
|Digital Signature| |1024|
| |RSA|2048|
| | |3072|
|HMAC|128, 256 & 384| |
|Encoding Scheme|ISO-8859-1|-|
|Structure|JSON|-|
|URL Checking|Xb|-|
|Compatibility|Xc|-|

a CBC, OFB, CFB and GCM; b Norton safe web; c Supports QR codes generated by other apps.

# 6. Experimental Results

We have conducted a user survey to get the user reactions about the BarSec Droid usage, and the level of trust for the provided security information. In order to compare the results with other security apps, we have chosen the most popular and secure QR code reader, i.e., QR Droid Private [7] that belongs to the popular and Crypto-based protection group. We followed the recommended sample size in [123] and conducted a survey with the help of 30 users who were undergraduate students from different colleges. They were asked to scan ten QR codes for each reader. Then, the users completed a survey that was built following the lines of three very popular usability surveys [124 – 126] and a usability survey on secure mobile applications [127]. Our survey includes the following ten points:

- Overall, I am satisfied with the ease of completing the tasks.
- Overall, I am satisfied with the amount of time it took to complete the tasks.
- Overall, I am satisfied with the support information (warnings and details messages).
- It is flexible?
- I would recommend it to a friend.
- I can effectively complete the tasks using this application.
- I am able to efficiently complete the tasks using this application.
- How much do you trust the security information in the application?
- Overall, I would like to use the application.
- Is the application visually appealing?

Each point had a five-point scale answer, described as: (1: very unsatisfied to 5: very satisfied). We have followed the answers evaluation method used on [127] by using paired t-test, which is a standard statistical method that compares the mean values of two groups. Paired t-test was used because the survey asked the user to evaluate 2 apps at a time.

# Table 7

shows the Means (the value before ±), Mean Standard Error ((MSE), the value after ±), and p-value results from participants’ feedback for BarSec Droid and QR Droid Private. Note that, in the t-test, when the p-value is less than 0.05, there is a statistically significant difference between two groups [128], and in this case the mean value is marked in bold in the table.

|App|Satisfaction of App|Satisfaction of App|Satisfaction of App|Satisfaction of App|Satisfaction of App|Satisfaction of App|Satisfaction of App|Satisfaction of App|Satisfaction of App|Satisfaction of App|
|---|---|
|Easy to Use|Time|Satisfaction|Support info|Security|Likely to Use|Visually Appealing|Flexible|Recommended|Effectively|Efficiently|
|BarSec Droid|4.2 ± 0.1|3.6 ± 0.2|3.0 ± 0.2|3.8 ± 0.2|4.0 ± 0.2|2.8 ± 0.2|3.4 ± 0.2|3.7 ± 0.2|3.5 ± 0.2|3.8 ± 0.2|
|[7]|2.6 ± 0.2|3.7 ± 0.2|3.8 ± 0.2|2.4 ± 0.2|2.8 ± 0.1|3.6 ± 0.2|3.3 ± 0.2|3.1 ± 0.2|2.7 ± 0.2|3.2 ± 0.2|
|p-value|0.000|0.647|0.001|0.000|0.000|0.022|0.842|0.014|0.007|0.019|

According to Table 7, BarSec Droid recorded better answers for easiness of use, security trust, being likely to use, recommended app, effectively and efficiently. On the other hand, QR Droid Private recorded a higher level of support information satisfaction and visually appealing, which reflects the application excellent design and options such as supporting multiple (29) languages. The results of the time of tasks and the flexibility recorded converged values, which reflects that BarSec Droid and QR Droid Private have acceptable time delay and flexible capabilities according to the user feedback.

# 7. Conclusions

This paper presents the most comprehensive evaluation for 100 barcode reader applications from a point of view of security and privacy issues. We have categorized these apps according to their features into five groups: URL security, Crypto-based security, Popular, Weak and, Save-privacy applications. Based on our analysis, we have proposed recommendations towards developing usable, secure and privacy-friendly applications and implemented BarSec Droid, a proof of concept Android app that follows our recommendations. Moreover, we have conducted user experiments to assess user experience on our app, compared to the most popular/secure QR code reader app. The results show that applying the design recommendations will increase the user security trust, ease of use alongside with the efficacy and effectiveness of scanning barcodes. As a future work, we plan to extend our analysis to cover more applications i.e., iOS and Windows phone apps. In addition, we plan to evaluate the available security mechanisms of QR code online contents such as: Google safe browsing and Norton Safe Web.

Author Contributions: Conceptualization and Methodology, H.A.M.W. and F.L.L.; Software, Data curation and Writing—original draft preparation, H.A.M.W.; Writing—review and editing, Supervision and Funding acquisition, F.L.L. All authors have read and agreed to the published version of the manuscript.

Funding: This research received no external funding.

Conflicts of Interest: The authors declare no conflict of interest.

# References

1. Denso Wave. QRcode.com DENSO WAVE. 2017. Available online: http://www.qrcode.com/en (accessed on 16 April 2020).
2. Zara Rizwan. Do People Use QR Codes in 2017? The Answer Will Definitely Surprise You. 2017. Available online: https://scanova.io/blog/blog/2017/08/04/do-people-use-qr-codes/ (accessed on 16 April 2020).
3. Dabrowski, A.; Krombholz, K.; Ullrich, J.; Weippl, E. QR Inception: Barcode-in-Barcode Attacks. In Proceedings of the 4th ACM CCS Workshop on Security and Privacy in Smartphones and Mobile Devices (SPSM’14), Scottsdale, AZ, USA, 7 November 2014; pp. 3–10.
4. Cai, H.L.; Yan, B.; Chen, N.; Pan, J.S.; Yang, H.M. Beautified QR code with high storage capacity using sequential module modulation. Multimed. Tools Appl. 2019, 78, 22575–22599. [CrossRef]
5. Akta, C. The Evolution and Emergence of QR Codes, 1st ed.; Cambridge Scholars Publishing: Cambridge, UK, 2017.
6. Focardi, R.; Luccio, F.; Wahsheh, H. Security Threats and Solutions for Two Dimensional Barcodes: A Comparative Study. In Computer and Network Security Essentials; Kevin, D., Ed.; Springer: Berlin/Heidelberg, Germany, 2018; pp. 207–219.
7. DroidLa. QR Droid Private. 2016. Available online: http://qrdroid.com/ (accessed on 16 April 2020).

# References

1. Wahsheh, H.; Luccio, F. Evaluating Security, Privacy and Usability Features of QR Code Readers. In Proceedings of the 5th International Conference on Information Systems Security and Privacy (ICISSP 2019), Prague, Czech Republic, 23–25 February 2019; pp. 266–273.
2. Yao, H.; Shin, D. Towards Preventing QR Code Based for Detecting QR Code Based Attacks on Android Phone Using Security Warnings. In Proceedings of the 8th ACM SIGSAC ASIA CCS, Hangzhou, China, 7–10 May 2013; pp. 341–346.
3. Google. Google Safe Browsing API, Website. Available online: https://developers.google.com/safe-browsing/ (accessed on 16 April 2020).
4. Phishtank. Phishtank API, Website. Available online: https://www.phishtank.com/ (accessed on 16 April 2020).
5. Krombholz, K.; Frühwirt, P.; Rieder, T.; Kapsalis, I.; Ullrich, J.; Weippl, E. QR Code Security–How Secure and Usable Apps Can Protect Users Against Malicious QR Codes. In Proceedings of the 2015 10th International Conference on Availability, Reliability and Security (ARES), Toulouse, France, 24–27 August 2015; pp. 230–237.
6. Dudheria, R. Evaluating Features and Effectiveness of Secure QR Code Scanners. In Proceedings of the International Conference on Cyber-Enabled Distributed Computing and Knowledge Discovery (CyberC), Nanjing, China, 12–14 October 2017; pp. 40–49.
7. KasperSky Lab. QR Code Reader and Scanner: App for Android. 2018. Available online: https://free.kaspersky.com/?cid=acq-gplay-lnk#mobile (accessed on 16 April 2020).
8. G Data Software AG. G DATA QR Code Scanner. 2018. Available online: https://www.gdata.de/ (accessed on 16 April 2020).
9. Google Inc. Google Play Store. 2018. Available online: https://play.google.com/store?hl=en (accessed on 16 April 2020).
10. NortonMobile. Norton Snap QR Code Reader. 2016. Available online: https://support.norton.com/sp/en/us/home/current/solutions/v64691018_EndUserProfile_en_us?client=norton&site=nrtn_en_US (accessed on 16 April 2020).
11. Trend Micro. QR Scanner-Free, Safe QR Code Reader, Zero Ads. 2018. Available online: https://www.trendmicro.com/en_us/business.html (accessed on 16 April 2020).
12. FANSec Lab Apps. Secure QR Code Scanner. 2018. Available online: https://play.google.com/store/apps/details?id=com.fansec.lab.security.secureqrcodescanner (accessed on 16 April 2020).
13. Madiff Net. QR & Barcode Security. 2017. Available online: https://play.google.com/store/apps/details?id=com.trustbookin.qrcodebarcodesecurity (accessed on 16 April 2020).
14. Dennings. Safe QR-Scanner & Generato. 2018. Available online: http://www.dennings.org/ (accessed on 16 April 2020).
15. KidControl Dev. Safe GeoTag QR Scanner. 2018. Available online: https://web.facebook.com/GeoTagQR?_rdc=1&_rdr (accessed on 16 April 2020).
16. Tengler, D. Crypto Message. 2018. Available online: https://play.google.com/store/apps/details?id=cz.crypto_message_free.apk (accessed on 16 April 2020).
17. Avira. Free QR Scanner. 2018. Available online: https://www.avira.com/ (accessed on 16 April 2020).
18. Browser Extension. QR Code Scanner & Barcode Reader for CM Browser 2018. Available online: http://www.cmcm.com/en-us/ (accessed on 16 April 2020).
19. SECUSO Research Group. QR Scanner (Privacy Friendly). 2016. Available online: https://secuso.aifb.kit.edu/index.php (accessed on 16 April 2020).
20. X and C Hi-Tech Inc. Scan 2D Social QR Code Scanner. 2016. Available online: http://www.scan2d.com/static/index.html (accessed on 16 April 2020).
21. iTechSol. Secure QR Barcode Scanner. 2018. Available online: https://play.google.com/store/apps/details?id=com.scanner.qr.barcode.reader.bar.codes (accessed on 16 April 2020).
22. Red Dodo. QR & Barcode Reader (Secure). 2014. Available online: http://reddodo.com/qr-barcode-scanner.php (accessed on 16 April 2020).
23. Tokoware. Private QR Reader Free. 2016. Available online: http://www.tokoware.com/ (accessed on 16 April 2020).
24. FancyApp. QR Code Reader Extreme. 2018. Available online: https://play.google.com/store/apps/details?id=com.fancyapp.qrcode.barcode.scanner.reader (accessed on 16 April 2020).

# Information 2020, 11, 217

# References

1. TeaCapps. QR & Barcode Reader. 2018. Available online: https://play.google.com/store/apps/details?id=com.teacapps.barcodescanner (accessed on 16 April 2020).
2. Ecrubit Consultancy Service. EC QR. 2018. Available online: http://www.ecrubit.com/ (accessed on 16 April 2020).
3. Application4u. Lightning QRcode Scanner. 2018. Available online: http://ww7.application-4u.com/ (accessed on 16 April 2020).
4. Scan. QR Code Reader. 2016. Available online: https://www.scan.me/ (accessed on 16 April 2020).
5. ZXing Team. Barcode Scanner. 2017. Available online: https://github.com/zxing/ (accessed on 16 April 2020).
6. Geeks.Lab. 2015. Barcode Scanner Pro. 2018. Available online: https://play.google.com/store/apps/details?id=com.geekslab.qrbarcodescanner.pro (accessed on 16 April 2020).
7. Gamma Play. QR & Barcode Scanner. 2018. Available online: https://play.google.com/store/apps/details?id=com.gamma.scan (accessed on 16 April 2020).
8. Barcode Scanner. QR & Barcode Scanner. 2018. Available online: https://barcodescannerblog.wordpress.com/ (accessed on 16 April 2020).
9. EZ to Use. Free QR Scanner: Bar Code Scanner & QR Code Reader. 2018. Available online: https://play.google.com/store/apps/details?id=app.qrcode (accessed on 16 April 2020).
10. I-Plex Technology. Fastest QR Barcode Reader: Scanner And Generator. 2018. Available online: https://play.google.com/store/apps/details?id=com.iplextech.barcode.scanner (accessed on 16 April 2020).
11. ECO MOBILE VN. QR Code Scanner: Barcode Scanner & QR Code Reader. 2019. Available online: https://play.google.com/store/apps/details?id=com.vtool.qrcodereader.barcodescanner (accessed on 16 April 2020).
12. Gfects. G-scan QR Code and Barcode Scanner. 2018. Available online: https://play.google.com/store/apps/details?id=com.gscan.app (accessed on 16 April 2020).
13. Gfects. G-tos NFC Writer and QR Code and NFC Reader. 2019. Available online: https://play.google.com/store/apps/details?id=com.gfects.app (accessed on 16 April 2020).
14. TWMobile. QR code reader QR Code Scanner. 2019. Available online: https://play.google.com/store/apps/details?id=tw.mobileapp.qrcode.banner (accessed on 16 April 2020).
15. Duy Pham (MMLab). QR Code Reader no Ads. 2019. Available online: https://play.google.com/store/apps/details?id=com.duyp.vision.qrcode.reader (accessed on 16 April 2020).
16. bestdeveloperteam. QR Code Scanner. 2019. Available online: https://play.google.com/store/apps/details?id=com.barcodereader.qrcodereader (accessed on 16 April 2020).
17. Barcode Scanner. Barcode Scanner. 2019. Available online: https://play.google.com/store/apps/details?id=com.qrcodescanner.barcodescanner (accessed on 16 April 2020).
18. Mobile Ecology Group. QR Scanner Pro: All QR & Barcode. 2019. Available online: https://play.google.com/store/apps/details?id=qrcode.reader.qrcode.scanner (accessed on 16 April 2020).
19. Hauyu. SmartScan QR Scanner & QR Code Scanner Smart Scan. 2019. Available online: https://play.google.com/store/apps/details?id=qr.barcode.reader.scanner.tool (accessed on 16 April 2020).
20. Best App-Top Droid Team. QR code reader-QR Code & Barcode Scanner. 2018. Available online: https://play.google.com/store/apps/details?id=com.tohsoft.qrcode (accessed on 16 April 2020).
21. Net2user Team. Net2user QR Code Scanner. 2019. Available online: https://play.google.com/store/apps/details?id=com.net2user.qrscanner (accessed on 16 April 2020).
22. 1MB. QR Scanner & Barcode Scanner 2019. 2019. Available online: https://play.google.com/store/apps/details?id=com.kitkats.qrscanner (accessed on 16 April 2020).
23. Best App-Top Droid Team. QR Code Reader- Barcode Scanner. 2018. Available online: https://play.google.com/store/apps/details?id=com.tohsoft.qrcode.lite (accessed on 16 April 2020).
24. Maheshandsons. My Secure Qrcode Generator & Barcode Scanner. 2018. Available online: https://play.google.com/store/apps/details?id=com.mandsons.QrCodeScanner (accessed on 16 April 2020).
25. Big Ocean Studio. QR Code Scanner & Code Reader-Scan Barcode. 2019. Available online: https://play.google.com/store/apps/details?id=com.bigoceanstudio.qr.code.scanner.code.reader.scan.barcode (accessed on 16 April 2020).
26. hopesj0314. QR CODE READER- Easy, Fast and Free. 2019. Available online: https://play.google.com/store/apps/details?id=com.hopej.android.go (accessed on 16 April 2020).
27. turbo01. ScanOne: Barcode and QR Scanner. 2019. Available online: https://play.google.com/store/apps/details?id=com.developer.scanone (accessed on 16 April 2020).

# Information 2020, 11, 217

# References

1. AapniApps. Qr Barcode Scanner: Scan Multiple Codes at once. 2019. Available online: https://play.google.com/store/apps/details?id=com.aapnitech.scannerapp (accessed on 16 April 2020).
2. Geegle Tech. QRCode-Secure, Free, Simple Barcode Scanner. 2018. Available online: https://play.google.com/store/apps/details?id=com.yy.adam.qrcode (accessed on 16 April 2020).
3. National. G.S. Best QR Code & Barcode Scanner. 2019. Available online: https://play.google.com/store/apps/details?id=com.qrcodescan (accessed on 16 April 2020).
4. Ulterior Services. QR Barcode Scanner and Generator. 2018. Available online: https://play.google.com/store/apps/details?id=com.ulterior.barcodescanner (accessed on 16 April 2020).
5. Hertikha. QR Code Reader. 2018. Available online: https://play.google.com/store/apps/details?id=com.perfect.codereader (accessed on 16 April 2020).
6. Dikamjit Borah. Super Ultimate QR Scanner. 2018. Available online: https://play.google.com/store/apps/details?id=com.dikamjitborah.hobarb.superqrscanner (accessed on 16 April 2020).
7. Spartan Studio Inc. QR Code Reader, Barcode Scanner: QR Code Generator. 2019. Available online: https://play.google.com/store/apps/details?id=com.qrcodereader.barcode.codescanner.generator (accessed on 16 April 2020).
8. TPCreative. QR Code & Barcode: Scanner, Reader, Creator. 2019. Available online: https://play.google.com/store/apps/details?id=tpcreative.co.qrscanner.free.release (accessed on 16 April 2020).
9. HAK Media Team. QR Code Scanner. 2018. Available online: https://play.google.com/store/apps/details?id=com.hak.qrbarcodescanner (accessed on 16 April 2020).
10. bghavocapps. QR & Barcode Scanner. 2018. Available online: https://play.google.com/store/apps/details?id=com.bghavocapps.qrandbarcodecodescannerapp (accessed on 16 April 2020).
11. SanjoyBiswas. Qr Scanner Pro:Fast & Secure Scanner. 2018. Available online: https://play.google.com/store/apps/details?id=com.qrdemo (accessed on 16 April 2020).
12. Apps Wing. Lightning QR Code Scanner: Business Card Generator. 2019. Available online: https://play.google.com/store/apps/details?id=com.appswing.qr.barcodescanner.barcodereader (accessed on 16 April 2020).
13. 4 Tech Solutions. Barcode Reader: Barcode Scanner- QR Code Scanner. 2019. Available online: https://play.google.com/store/apps/details?id=com.fourtechsolutions.barcodescanner_barcodereader (accessed on 16 April 2020).
14. PRO APP Master. QR Code Master&Barcode Scanner-Free Safe Fast. 2019. Available online: https://play.google.com/store/apps/details?id=oms.mmc.qrscan (accessed on 16 April 2020).
15. Karmkeeda labs. Qr Code Scanner. 2018. Available online: https://play.google.com/store/apps/details?id=com.appybuilder.videosongs733.Barcode (accessed on 16 April 2020).
16. danny apps. QR Code Reader. 2019. Available online: https://play.google.com/store/apps/details?id=com.qrcode.reader.codebar (accessed on 16 April 2020).
17. Unger, A. SafeQR. 2018. Available online: https://play.google.com/store/apps/details?id=biz.ungerware.safeqr (accessed on 16 April 2020).
18. JLeagues. QR Code Reader. 2017. Available online: https://play.google.com/store/apps/details?id=com.zerg.zxing (accessed on 16 April 2020).
19. Pratik@Devloper. Fast QR and Barcode Scanner. 2018. Available online: https://play.google.com/store/apps/details?id=com.technicalblogger20.QR_and_Barcode_scanner (accessed on 16 April 2020).
20. SOLEZERO.COM. QR Code Secret. 2019. Available online: https://play.google.com/store/apps/details?id=com.solezero.android.qrcodesecret (accessed on 16 April 2020).
21. liliandroid. enQRCode: My Encrypted MSG-QR Code. 2019. Available online: https://play.google.com/store/apps/details?id=com.liliandroid.enqrccmyencryptedmsg (accessed on 16 April 2020).
22. Green Apple Studio. QR Code Reader. 2019. Available online: https://play.google.com/store/apps/details?id=com.apple.qrcode.reader (accessed on 16 April 2020).
23. SaiFinTex. Secret QrCode. 2019. Available online: https://apkpure.com/secret-qrcode/org.saifintex.qrcode (accessed on 16 April 2020).
24. pak developer master. QR Code Scanner & Generator 2019. 2019. Available online: https://play.google.com/store/apps/details?id=qrcode.masterapps.com.pak (accessed on 16 April 2020).
25. Iterative Solution Limited. Global Input App. 2018. Available online: https://play.google.com/store/apps/details?id=uk.co.globalinput (accessed on 16 April 2020).

# Information 2020, 11, 217

# References

1. Sory Apps. Simple QR Reader-Privacy. 2019. Available online: https://play.google.com/store/apps/details?id=es.soryapps.qrreader (accessed on 16 April 2020).
2. Tokoware. Private QR Premium. 2016. Available online: https://play.google.com/store/apps/details?id=com.tokoware.privateqrpremium (accessed on 16 April 2020).
3. Color Phone Team & QR Code Scanner. QR Code Reader Free -QR Reader For Android. 2019. Available online: https://play.google.com/store/apps/details?id=com.maqr.barcode.free.qrandbarcodescanner.mavach.qrcode.reader.qrcodereader.qrcodescanner.quickbarecodescanner (accessed on 16 April 2020).
4. Krow. QR Code Reader. 2019. Available online: https://play.google.com/store/apps/details?id=krow.dev.qrcode (accessed on 16 April 2020).
5. InShot Inc. Free QR Scanner- Barcode Scanner, QR Code Reader. 2019. Available online: https://play.google.com/store/apps/details?id=qrscanner.barcodescanner.barcodereader.qrcodereader (accessed on 16 April 2020).
6. Darren Dodgen. Inspire QR Code. 2019. Available online: https://play.google.com/store/apps/details?id=com.b.greenscanner (accessed on 16 April 2020).
7. Apps360 Team. QR and Barcode Scanner. 2019. Available online: https://play.google.com/store/apps/details?id=com.qrcode.barcode.scanner.reader.generator.free (accessed on 16 April 2020).
8. Modulets. Green QR Code Reader. 2018. Available online: https://play.google.com/store/apps/details?id=net.modulets.greenqr (accessed on 16 April 2020).
9. Buymobile. QR Code Reader and Bar Code Code Reader. 2018. Available online: https://play.google.com/store/apps/details?id=info.recipe.user.qr_bar (accessed on 16 April 2020).
10. JarDroid. Best QR Code Scanner 2017. 2017. Available online: https://play.google.com/store/apps/details?id=com.qrcodescanner.qrcodegenerator.sacnner (accessed on 16 April 2020).
11. EasyToolsDev. QR Code and Barcode Scanner-Free & Fast. 2018. Available online: https://play.google.com/store/apps/details?id=com.qrcode.scanner.reader.mobi (accessed on 16 April 2020).
12. LT TEAM. Smarte: QR Barcode Scanner e Generatore. 2017. Available online: https://play.google.com/store/apps/details?id=com.smarttoolapp.qr.barcode.scanner (accessed on 16 April 2020).
13. E-swamera. Qr Scanner. 2017. Available online: https://play.google.com/store/apps/details?id=com.scan.qrbarcodeScanner (accessed on 16 April 2020).
14. Abqarie Studio. QR Code Scanner & Generator. 2018. Available online: https://play.google.com/store/apps/details?id=com.abqarie.qrcodescannerandgenerator (accessed on 16 April 2020).
15. Rstream Labs. QR Scanner & Barcode Reader PRO. 2018. Available online: https://play.google.com/store/apps/details?id=com.riatech.qrscanner (accessed on 16 April 2020).
16. Mysirg.net. Lightning QR Scanner. 2018. Available online: https://play.google.com/store/apps/details?id=io.makeroid.sandy148101.QR_Scanner (accessed on 16 April 2020).
17. LaHaSoft. Best QR code and Barcode Scanner. 2018. Available online: https://play.google.com/store/apps/details?id=com.lahastudio.barcode&hl=en_US (accessed on 16 April 2020).
18. Indigo Apps Studio. QR Code Scanner-QR Code Reader & QR Reader: Scanner. 2019. Available online: https://play.google.com/store/apps/details?id=com.indigoapps.qrquickscanner (accessed on 16 April 2020).
19. MV Group. QR Code Message. 2017. Available online: https://play.google.com/store/apps/details?id=com.collalab.qrcodemessage (accessed on 16 April 2020).
20. Arth InfoTech. QR Code. 2019. Available online: https://play.google.com/store/apps/details?id=com.myapp.scanner.qercode (accessed on 16 April 2020).
21. Apps Orange Tech. Inc. QR Reader: Simple QR Code Scanner. 2019. Available online: https://play.google.com/store/apps/details?id=com.qr.code.decoder.scanner.qr.reader (accessed on 16 April 2020).
22. DEVappy. Pro QR Reader. 2019. Available online: https://play.google.com/store/apps/details?id=com.lyricand.codebar.qrcode (accessed on 16 April 2020).
23. Sustainable App Developer. QR Code Reader. 2018. Available online: https://play.google.com/store/apps/details?id=com.qrcodereaderapp (accessed on 16 April 2020).
24. KInc. Bar Code Reader- Generator: Free 2019. 2019. Available online: https://play.google.com/store/apps/details?id=com.kincapps.qrcodescanner (accessed on 16 April 2020).
25. Habib KHLIFI. QR Code Reader. 2019. Available online: https://apkpure.com/it/qr-code-reader/qr.code.reader (accessed on 16 April 2020).

# Information 2020, 11, 217

# References

1. R2 Development. QR Util-Scan and Create QR. 2019. Available online: https://play.google.com/store/apps/details?id=com.r2devs.qrutil (accessed on 16 April 2020).
2. AR Inc. QR Coba-QR Code Generator & Scanner. 2019. Available online: https://play.google.com/store/apps/details?id=qrcode.arinc.com.qrcode (accessed on 16 April 2020).
3. Joe North. QR Code Scanner. 2018. Available online: https://play.google.com/store/apps/details?id=com.north.qrcode.barcode.reader.scanner.free (accessed on 16 April 2020).
4. mr.newbie limited. EPTLS QR Scan. 2015. Available online: https://play.google.com/store/apps/details?id=com.mrnewbie.eptls (accessed on 16 April 2020).
5. Gestrs. Gestrs QR Scanner- Ad free, Fast & Secure. 2019. Available online: https://play.google.com/store/apps/details?id=com.qrcodescan.gestrs (accessed on 16 April 2020).
6. Liu, T.; Yan, B.; Pan, J. Color Visual Secret Sharing for QR Code with Perfect Module Reconstruction. Appl. Sci. 2019, 9, 4670. [CrossRef]
7. European Union Agency for Network and Information Security (ENISA). Algorithms, Key Size and Parameters Report—2014. 2014. Available online: https://www.enisa.europa.eu/publications/algorithms-key-size-and-parameters-report-2014 (accessed on 16 April 2020).
8. Focardi, R.; Luccio, F.; Wahsheh, H.A.M. Usable Cryptographic QR Codes. In Proceedings of the 19th International Conference on Industrial Technology, Lyon, France, 20–22 February 2018; pp. 1664–1669.
9. GitHub. ZXing Project Home. 2018. Available online: https://github.com/zxing/zxing/ (accessed on 16 April 2020).
10. D’Orazio, C.J.; Choo, K.K.R. A technique to circumvent SSL/TLS validations on iOS devices. Future Gener. Comput. Syst. 2017, 74, 366–374. [CrossRef]
11. Varela-Vaca, A.; Gasca, R.; Ceballos, R.; Gómez-López, M.; Torres, P. CyberSPL: A Framework for the Verification of Cybersecurity Policy Compliance of System Configurations Using Software Product Lines. Appl. Sci. 2019, 9, 5364. [CrossRef]
12. Reeder, R.W.; Felt, A.P.; Consolvo, S.; Malkin, N.; Thompson, C.; Egelman, S. An Experience Sampling Study of User Reactions to Browser Warnings in the Field. In Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems, Montreal, QC, Canada, 21–26 April 2018; p. 512.
13. Focardi, R.; Luccio, F.; Wahsheh, H. Usable Security for QR Code. J. Inf. Secur. Appl. 2019, 48, 102396. [CrossRef]
14. Symantec Corporation. Norton Safe Web. 2018. Available online: https://safeweb.norton.com/ (accessed on 16 April 2020).
15. Albert, W.; Tullis, T. Measuring the User Experience: Collecting, Analyzing, and Presenting Usability Metrics; Morgan Kaufmann, Amsterdam, The Netherlands, 2013.
16. Gary Perlman. After Scenario Questionnaire. 2018. Available online: http://garyperlman.com/quest/quest.cgi?form=ASQ (accessed on 16 April 2020).
17. Gary Perlman. Computer System Usability Questionnaire. 2018. Available online: https://garyperlman.com/quest/quest.cgi?form=CSUQ (accessed on 16 April 2020).
18. Gary Perlman. USE Questionnaire: Usefulness, Satisfaction, and Ease of Use. 2018. Available online: https://garyperlman.com/quest/quest.cgi?form=USE (accessed on 16 April 2020).
19. Farb, M.; Lin, Y.H.; Kim, T.H.J.; McCune, J.; Perrig, A. Safeslinger: Easy-to-Use and Secure Public-Key Exchange. In Proceedings of the 19th annual international conference on Mobile Computing & Networking, London, UK, 21–25 September 2013; pp. 417–428.
20. StatsDirect Limited. P-Value. 2018. Available online: https://www.statsdirect.com/help/basics/p_values.htm (accessed on 16 April 2020).

©c 2020 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (http://creativecommons.org/licenses/by/4.0/).