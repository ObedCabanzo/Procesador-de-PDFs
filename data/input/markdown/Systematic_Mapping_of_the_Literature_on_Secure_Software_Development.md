

# Systematic Mapping of the Literature on Secure Software Development

HERNAN NINA 1,2, (Senior Member, IEEE), JOSÉ ANTONIO POW-SANG1, (Senior Member, IEEE), AND MÓNICA VILLAVICENCIO3

1Maestría en Informática, Pontificia Universidad Católica del Perú, Lima 15088, Peru

2Carrera Profesional de Ingeniería de Sistemas, Universidad de Lima, Lima 15023, Peru

3Facultad de Ingeniería en Electricidad y Computación, Escuela Superior Politécnica del Litoral, 090902 Guayaquil, Ecuador

Corresponding author: Hernan Nina (hernan.nina@pucp.edu.pe)

Received January 22, 2021, accepted February 15, 2021, date of publication February 26, 2021, date of current version March 9, 2021.

Digital Object Identifier 10.1109/ACCESS.2021.3062388

# ABSTRACT

The accelerated growth in exploiting vulnerabilities due to errors or failures in the software development process is a latent concern in the Software Industry. In this sense, this study aims to provide an overview of the Secure Software Development trends to help identify topics that have been extensively studied and those that still need to be. Therefore, in this paper, a systematic mapping review with PICo search strategies was conducted. A total of 867 papers were identified, of which only 528 papers were selected for this review. The main findings correspond to the Software Requirements Security, where the Elicitation and Misuse Cases reported more frequently. In Software Design Security, recurring themes are security in component-based software development, threat model, and security patterns. In the Software Construction Security, the most frequent topics are static code analysis and vulnerability detection. Finally, in Software Testing Security, the most frequent topics are vulnerability scanning and penetration testing. In conclusion, there is a diversity of methodologies, models, and tools with specific objectives in each secure software development stage.

# INDEX TERMS

Software development, security, requirements, design, construction, testing, vulnerability, systematic mapping review.

# I. INTRODUCTION

A study by the US Department of Homeland Security shows that more than 90% of cyber-attacks are not due to defects in cryptography, networks, or hardware, but due to vulnerabilities generated in software development [1]. Furthermore, the increase in malicious activities targeting software products and software security weaknesses has become a significant problem for the software development process. Likewise, it is necessary to address security issues from the beginning of the software development life cycle (and in each phase) instead of facing them by creating patches when the software is in the production phase [2]–[4]; therefore, a comprehensive model is needed to adapt security activities to the software development process [6]. The secure software development process comprises software requirements security, software design security, software construction security, and software testing security. This process aims to enrich security requirements, use threat models methodologies during software design, and apply best security practices for coding, code reviews, and tests [5]. To increase the security level of software products, this process should be continuously updated [5], [7]; hence, studies showing the trends in methodologies, notations, tools, and techniques are required.

Moreover, a systematic mapping study with an updated overview of trends in secure software development is necessary to identify the most relevant topics in the secure software development process and to complement existing studies which have a variety of objectives and context. For example, some systematic mapping reviews focus on: agile methodologies’ security requirements; specific applications (e.g. Cyber-physical System), particular methods (e.g. problem frames or threat analysis), quality assessment, SWOT analysis, among others [8]–[14].

This paper is structured as follows: Section II describes the research methodology, section III presents the results of the systematic mapping study, and section IV poses the conclusions and future works.

36852 This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

VOLUME 9, 2021

# EEE Access

# H. Nina et al.: Systematic Mapping of the Literature on Secure Software Development

# Study Planning

# Searching for Studies

# Study Selection

# Assessing Study Quality

# Data Extraction and Classification

# Analysis

# Reporting

FIGURE 1. Process steps for systematic mapping studies.

# II. RESEARCH METHODS

This systematic mapping follows the guidelines for performing systematic literature reviews in software engineering proposed by Kitchenham and Charters [15] and the guidelines for systematic mapping studies in security engineering recommended by Felderer and Carver [16]. Figure 1 illustrates the steps described to carry out systematic mapping studies.

Each process of the systematic mapping study in secure software development is presented below.

# A. STUDY PLANNING

In this phase, the research questions must be formulated. To do so, the PICo technique [17] was applied, as follows:

- Population: Software development.
- Interest: Secure software.
- Context: The context corresponds to the sector of the Software development industry.

As a result, five research questions were stated for this mapping study (see Table 1).

# B. SEARCHING FOR STUDIES

For the present study, the indexed bibliographies databases were used: Scopus, Web of Science, IEEE Xplore, and ACM Digital Library. These databases are frequently used in systematic mapping studies in the Software Engineering discipline and have automated search tools that allow an adequate level of coverage for the subject studied. Table 2 illustrates the selected sources for this mapping study.

The search for scientific articles in the above mentioned databases was carried out according to the following procedure:

- Keywords: Two keywords were obtained by decomposing the research questions: ‘‘software development’’ and ‘‘secure software’’.
- Synonyms: Synonyms were created for ‘‘software development’’ which correspond to the following terms: ‘‘software engineering’’, ‘‘software process’’, ‘‘software construction’’, and ‘‘software project’’. The following terms were used for the keyword ‘‘secure software’’: ‘‘software security’’, ‘‘security requirement’’, ‘‘security attribute’’, ‘‘software vulnerability’’.
- Search strings: Search strings were generated using logical operators: OR for synonyms and AND for combine keywords. Table 3 shows the string used in each database considering studies published in English between 2014 and 2019. The total number of publications found until June 10th, 2019 was 867.
- Filtering articles: Articles with a blank abstract or a language other than English were deleted.

# C. STUDY SELECTION

For the final selection of the articles, the inclusion and exclusion criteria shown in Table 4 were used.

VOLUME 9, 2021

# H. Nina et al.: Systematic Mapping of the Literature on Secure Software Development

# TABLE 3. Search strings by database.

# TABLE 4. Inclusion and exclusion criteria.

# TABLE 5. Summary of results.

After applying the inclusion and exclusion criteria and filtering duplicates, 528 articles were selected. Table 5 shows the summary of the search process.

For selecting the articles, the title and abstract were read. However, full-text reading was necessary in 49 studies.

# D. ASSESSING STUDY QUALITY

Considering that a large number of studies were retrieved; one reviewer, the first author, filtered the papers applying the inclusion and exclusion criteria [18]. Next, actions were taken by the second author to evaluate the final set of articles to reduce the validity threat. The second author checked the extraction to reduce the bias. The quality assessment of selected studies was performed based on their credibility, integrity, and relevance to answer the research questions.

# E. DATA EXTRACTION

The extraction of the relevant data from the selected studies was performed using a classification scheme (see Figure 2).

36854

VOLUME 9, 2021

# H. Nina et al.: Systematic Mapping of the Literature on Secure Software Development

# Sub-phases in the security requirements stage

- Elicitation
- Analysis
- Specification
- Validation

# Methods used in security requirements

- Approach Security Requirements Engineering
- Misuse Cases
- Fuzzy Analytic Hierarchy Process
- Machine Learning Technique
- Threat Modeling
- Security Patterns
- UMLsec
- Structured Object-Oriented Formal Language
- Non-Functional Requirements Modeling
- Architecture Modeling
- Identify and Access Management
- Develop an Encryption Strategy
- Security Design Principles

# Topics in the secure code building stage

- Static Code Analysis
- Standards and Conventions
- Compiler; library; and execution environment
- Handle Errors
- Find Security Issues Early
- Dynamic Code Analysis

# Vulnerabilities in the secure code construction stage

- Standards on vulnerabilities
- Detecting vulnerabilities
- Exploit vulnerabilities prevention
- Vulnerability Response and Disclosure
- Fix the Vulnerability
- Mitigation vulnerabilities
- Predicting vulnerabilities
- Assessment potentially vulnerability
- Classification vulnerabilities
- Software vulnerability mining
- Vulnerability Scanning
- Penetration testing
- Fuzz testing

# Software Testing Security

- Static Analysis Security Testing
- Reverse Engineering and software disassembling
- Automatic patch generation
- Dynamic Analysis Security Testing
- Code review coverage
- Dynamic symbolic execution (DSE)
- Automated Testing
- Security principle

# Types of papers

- Security application domains
- Main trends
- Type of software application
- Non-traditional life cycle model
- Secure software development model
- Contributions to the development of secure software
- Artificial intelligence techniques
- Problems encountered by developers

# FIGURE 2. Classification scheme for data extraction.

based on a set of recommended rules and practices in secure software development obtained from: the Software Engineering Body of Knowledge (SWEBOK), ISO/IEC/IEEE 12207:2017 Standard, Software Security Assurance State of the Art Report (SOAR), and Software Assurance Forum for Excellence in Code (SAFECode).

# III. RESULTS AND ANALYSIS

This section presents the results for each research question and consequently provides an overview of the secure software development process trends. A way to determine the relevance of security related aspects encountered in the context of software development can be through their frequency (i.e. the number of times that an aspect is reported in the analyzed documents).

# A. RQ1: WHAT ARE THE MAIN TRENDS IN SECURE SOFTWARE DEVELOPMENT?

The main trends in the development of Secure Software according to systematic mapping are classified on the

VOLUME 9, 2021

36855

# H. Nina et al.: Systematic Mapping of the Literature on Secure Software Development

# TABLE 6. Number of articles by main trends.

|Soliware|Sofiware Testing|Requirements Security|
|---|---|---|
|14%|20%| |
|Software Construction|Software Design Security| |
|42%|24%| |

# FIGURE 3. Classification by phases of secure software development.

First, the publications were classified based on the phases of secure software development. Likewise, according to the Software Engineering Body of Knowledge (SWEBOK) and CSSLP Certification, the phases of the construction of Secure Software correspond to the requirements, design, coding, and testing phase of secure software [19], [20]. Figure 3 illustrates that 267 (42%) of 528 studies focus on the coding phase of secure software, being this the first topic of interest, followed by the design, requirements, and testing phases. These results are similar to a previous systematic mapping study on security in the software development life cycle carried out with publications between 1980 and 2015, where coding, design, and requirements reached 42%, 29%, and 19%, respectively [14].

Second, the security principles were analyzed using the ISO/IEC/IEEE 12207-2017 standard and CSSLP Certification Program definitions – see Figure 4. The most frequently reported security principles are confidentiality, integrity, and availability. They were identified in 42 studies (8% of 528 articles) by reviewing the entire content of some articles.

Third, the articles were classified based on the type of types of papers recommended in [16] and [21], (see Table 7). As it can be observed, the evaluation research type is reported more frequently (53% of all reviewed papers). This kind of research implements a technique in practice or studies a problem in practice [16]. Only 23 papers reported systematic reviews and mappings.

# Table 8

presents a closer view of the evaluation and validation research types, showing that a higher proportion corresponds to the case study research type followed by experiments.

Fourth, the articles were also sorted out by the security application domains, resulting in 64 studies; the predominant domain was government – see Table 9. Some of the articles propose government frameworks for secure software development (e.g. Information technology services to the Brazilian Government, Malaysian public sector for in-house web application development, Chinese IT security standards, etc).

Fifth, the type of software application was obtained from 209 articles that contained that information. Results are shown in Figure 5 where Web applications (33%) are the most referred since they are prey to constant attacks that are difficult to control. Also, large enterprise software presents a latent security concern because managing bulky assets, components, and a considerable amount of code is complex. Likewise, cyber-physical systems must be completely secure, since these are sensitive applications that integrate physical systems with software (e.g. systems that manage the operation of electrical networks). Similarly, emerging applications such as IoT applications are gradually becoming an attractive attack vector due to their limited security.

Sixth, the studies were classified according to the type of software life cycle model. To do so, it was necessary to review the entire content of some articles. Figure 6 shows that the most referred were the agile methodologies being.

36856

VOLUME 9, 2021

# H. Nina et al.: Systematic Mapping of the Literature on Secure Software Development

# Confidentiality

29%

# Integrity

21%

# Availability

21%

# Authentication

10%

# Authorization

8%

# Traceability

4%

# Data encryption

3%

# Non-repudiation

3%

10        15        20        25        30        35

Number of papers

# FIGURE 4. Frequency of papers by security principle.

# TABLE 7. The trend in the types of studies related to secure software development.

# TABLE 8. The evaluation research and validation research types reported.

# TABLE 9. Security application domain.

the Scrum framework and the dynamic software develop-

ment those that stand out. It was also found that agile

methodologies are not the preferred option for developing

large-scale projects, security-critical software projects, and

projects where requirements are known in advance. Waterfall

methodologies are preferred in those types of projects [22].

VOLUME 9, 2021

36857

# H. Nina et al.: Systematic Mapping of the Literature on Secure Software Development

# Other applications

|Web application|5%|
|---|---|
|IoT|33%|
|Mobile application|9%|
|Cyber-physical systems|11%|
|Large project Software|18%|
|Open Source|16%|

FIGURE 5. Classification of papers by type of application.

# TABLE 10. The secure software development model.

|Agile methodologies|61%|
|---|---|
|Model-Driven Development|27%|
|Devops|12%|

Number of papers

FIGURE 6. Classification of papers by non-traditional life cycle model.

Seventh, we looked for secure software development models among the articles. Table 10 illustrates the results obtained from reading 44 studies, where it can be observed that the Comprehensive Lightweight Application Security Process (OWASP - CLASP) and the Microsoft Security Development Lifecycle (SDL) are the most commonly referred. The models that do not appear in the studies despite their popularity are Security Apple Developer, Web Application Security Consortium (WASC), and SANS information security training. Apart from secure software development models, there are also organizations in the world that lead security issues such as Central Illinois Center of Excellence for Secure Software (CICESS), Illinois Central College (ICC), GDPR (General Data Protection Regulation), Malaysian Public Service Organization (MPS), Department of Defense (DoD), European Space Agency (ESA).

Eighth, the contributions that the researchers propose in their studies appear in Table 11. Models, methodologies, and tools are the most generally reported. A model is a graphic or mathematical description of a system with its respective properties; a methodology is a particular set of procedures; and a tool is the implementation of a process.

Ninth, we look at trends in the use of Artificial Intelligence techniques for secure software development. Figure 7 illustrates the result of 52 studies related to this issue. Machine learning techniques are undoubtedly trending in secure software development, among them the Bayesian network, Support Vector Machine (SVM), Long Short-Term Memory model (LSTM), K-Nearest Neighbor (KNN), Principal Component Analysis (PCA), Naive Bayes, and frequency-reverse document frequency TF-IDF.

Finally, Figure 8 presents the classification of papers according to the problems identified by developers regarding.

36858

VOLUME 9, 2021

# H. Nina et al.: Systematic Mapping of the Literature on Secure Software Development

# TABLE 11. Contributions to the development of secure software.

|Machine Learning|54%|
|---|---|
|Natural language processing|16%|
|Data mining|10%|
|Deep learning| |
|Ontology for security knowledge| |
|Genetic algorithm|3%|
|Security Knowledge Base|3%|

# FIGURE 7. Classification of articles by artificial intelligence techniques.

10 15 20 25 30 35

Number of papers

# Need for assistance and training

|42%|Validation|14%|
|---|---|---|
|Elicitation|31%| |
|Lack of knowledge and skills|30%| |
|Need for security expert|16%| |
|Feel overloaded|12%| |

# FIGURE 8. Problems encountered by developers.

# FIGURE 9. Sub-phases in the security requirements stage.

secure software development. As it can be seen, what developers require the most is assistance and training to develop secure software. This is understandable since the analyzed articles report that developers: lack of knowledge or skills to build these kind of applications, have the need for a security expert to guide them, and feel overloaded or have complex development activities to perform. Some proposals consider it essential to change the developer’s mindset to make security a priority in software development. In this respect, security training helps, but developers find it challenging to apply it into their programming tasks [23]. It is important to consider that awareness of security issues is generated through several avenues, including company processes, standards, practices, and training, as well as the contextual factors that drive the focus on security [24].

VOLUME 9, 2021

36859

# H. Nina et al.: Systematic Mapping of the Literature on Secure Software Development

# TABLE 12. Sub-phases in the security requirements stage.

|Misuse Cases|299|
|---|---|
|Approach Security Requirements Engineering|17%|
|Fuzzy Analytic Hierarchy Process|9%|
|Machine Learning Technique|9%|
|Problem Frames|6%|
|UMLsec|6%|
|Non-Functional Requirements Modeling|4%|
|Structured Object-Oriented Formal Language|4%|
|Others|17%|

# FIGURE 10. Methods used in security requirements.

# B. RQ2: WHAT ARE THE MOST PROMINENT ACTIVITIES, AND WHAT METHODS ARE PREVALENT IN SOFTWARE REQUIREMENTS SECURITY?

Security requirements are divided into two categories. The first category includes software functions that implement security policies or that are required for security reasons. The second category is related to the probability that software security is threatened [19], [25]. Therefore, it is necessary to consider security aspects from the early phases of development. The first phase should identify the software security requirements and lay the foundation with high-level requirement models to continue developing secure software in the next phases [5].

In the secure software requirements phase, the sub-phases of elicitation, analysis, specification, and validation are carried out. Figure 9 and Table 7 shows the classification of 154 papers related to the requirement phase, being elicitation and analysis the sub-phases commonly referred. In the elicitation sub-phase, the sources of security requirements are identified based on the application’s goals, domain, and stakeholders. For its part, the analysis sub-phase classifies and identifies limits, and detects and resolves conflicts between requirements. Finally, the specification sub-phase writes the requirements in a formal document to be evaluated in the requirements validation sub-phase.

Figure 10 and Table 13 presents the security requirements methods or techniques identified in 70 papers. These methods or techniques aim to identify precise requirements, without ambiguities, and balanced them with other software quality attributes such as usability and durability. The misuse

36860

VOLUME 9, 2021

# H. Nina et al.: Systematic Mapping of the Literature on Secure Software Development

# TABLE 13. Methods used in security requirements.

|Security in component-based software|20%|
|---|---|
|Threat Modeling|19%|
|Security Patterns|18%|
|Design Review Activities|9%|
|Architecture Modeling|8%|
|Identity and Access Management| |
|Develop an Encryption Strategy| |
|Security Design Principles|4%|
|Others|8%|

# FIGURE 11. Security issues in the secure software design phase.

10 20 30 40

Number of papers

Case is more frequently highlighted, which is used to elicit security requirements and identify potential threats in the use cases. Other methods or techniques were identified with the same objective and similar tasks, but with different names and approaches to tackle security. Likewise, many of the techniques derive from Security Requirements Engineering, but there is an interest in applying methods based on machine learning and agile methodologies. Also, for the prioritization of security requirements, the Fuzzy - Analytic Hierarchy Process method is reported. In addition, to represent security requirements, UML diagram extensions are used in techniques such as UMLsec. Finally, it is not a matter of choosing the best technique but looking at how they can complement each other. For example, requirements for safety, and security, usability, and reliability.

# C. RQ3: WHAT ARE THE TRENDS IN SOFTWARE DESIGN SECURITY?

According to the ISO/IEC/IEEE 12207-2017 standard definitions, software design consists of two activities: software architectural design and software detailed design. Software design security deals with the design of software modules to meet security objectives specified in the security requirements stage. Early attention to security issues, such as captured security requirements and design an architecture, can decrease the likelihood of weaknesses in design [25].

VOLUME 9, 2021 36861

# H. Nina et al.: Systematic Mapping of the Literature on Secure Software Development

# TABLE 14. Security issues in the secure software design phase.

|Static Code Analysis|25%|
|---|---|
|Compiler; library; and execution environment|13%|
|Coding Standards and Conventions|13%|
|Handle Data Safely|11%|
|Handle Errors|10%|
|Find Security Issues Early|6%|
|Dynamic Code Analysis|6%|
|Others|14%|

# FIGURE 12. Topics in the secure code building stage.

In the present study, 149 papers (28% of the total sample) are related to secure software design topics. Figure 11 and Table 14 shows that security in a component-based software system, threat modeling, and security patterns are trends in design. Security in a component-based software system is an option to develop software using third-party software components since many times the security risks that can be inherited from such components are not taking into account, whether we use commercial off-the-shelf-products (COTS) or open-source software (OSS). Thread Modeling is an activity best executed in the software design phase and has the purpose of identifying the attacks that the software must withstand using the best defense strategy [26]. Security patterns correspond to structured solutions for recurring security problems and are reusable to design secure applications. Security Patterns allow software architects and designers to produce systems that meet their security requirements, are maintainable and extensible from the smallest to the most extensive systems. [27], [28].

Other topics are design review activities performed at the end of the detailed design stage and before starting the coding and testing phases [20], [25]. Architecture modeling includes the modeling of the architecture for comprehensive security analysis and the identification of possible attacks. Likewise, for architectural modeling, UML diagrams are used to represent entities, resources, privileges, safeguards, and

# H. Nina et al.: Systematic Mapping of the Literature on Secure Software Development

# TABLE 15. Topics in the secure code building stage.

|Detecting vulnerabilities|30%|
|---|---|
|Exploit vulnerabilities prevention|16%|
|Vulnerability Response and Disclosure|15%|
|Fix the Vulnerability|12%|
|mitigation vulnerabilities|11%|
|Predicting vulnerabilities|7%|
|Assessment potentially vulnerability|5%|
|Classification vulnerabilities|4%|
|Software vulnerability mining|1%|

# FIGURE 13. Vulnerabilities in the secure code construction stage.

policies [25]. Regarding identity and access management, the ISO 24760 standard defines them as a set of processes and policies involved in managing the life cycle of digital identity. Encryption Strategy is the encryption mechanism used to protect propagated data or inadvertent alteration, either of stored or transmitted data. This mechanism is considered comfortable, efficient, and cost-effective in the design process [26]. Finally, the security design principles establish general rules and guidelines for design.

# D. RQ4: WHAT ARE THE MOST FREQUENT TOPICS IN SOFTWARE CONSTRUCTION SECURITY?

Software construction security refers to writing the code for specific situations to deal with security considerations. Encryption of security in software can be achieved by following the rules recommended in the Software Engineering Body of Knowledge (SWEBOK) [19]. These rules emphasize that the Software modules must be as small as possible, with validated and documented privileges, and with the ability to avoid sharing objects in memory with other programs. Figure 12 and Table 15 shows the classification of 160 studies related to secure code construction, where the most frequent topic corresponds to Static code analysis (25%). The classification is based on the approach made by SafeCode and the Information Assurance Technology Analysis Center (IATAC) [19], [20].

A vulnerability is a weakness expressed in errors or flaws in the software, which can be exploited by an attacker [29]. According to Andy Ozment, there are three leading causes of vulnerabilities in software: loss of motivation of

VOLUME 9, 2021 36863

# H. Nina et al.: Systematic Mapping of the Literature on Secure Software Development

# TABLE 16. Vulnerabilities in the secure code construction stage.

|National Vulnerability Database (NVD)|21%|
|---|---|
|Common Vulnerabilities and Exposures (CVE)|170|
|Comton Weakness Enumeration (CWE)|1280|
|Vulnerability Scoring System (CVSS)|10|
|SQL injection (SQLIA)|10%|
|Buffer overflow vulnerability| |
|Android Common Mobile Vulnerability|500|
|Cross-site scripting (XSS)|400|
|Others|12%|

# FIGURE 14. Standards on vulnerabilities.

# TABLE 17. Standards on vulnerabilities.

programmers due to constant changes in software require- for the construction of secure software [25]. Figure 13 and Table 16 shows the classification of vulnerability issues in 159 studies. As it can be noticed, the two most referred

36864

VOLUME 9, 2021

# H. Nina et al.: Systematic Mapping of the Literature on Secure Software Development

# Vulnerability Scanning

16%

# Penetration Testing

14%

# Fuzz Testing

13%

# Static Analysis Security Testing

13%

# Reverse Engineering and Software Disassembling

11%

# Automatic Patch Generation

# Dynamic Analysis Security Testing

50

# Code Review Coverage

50/

# Dynamic Symbolic Execution (DSE)

5"0

# Automated Testing

3%/

# Others

12%

10   12          16   18    20

Number of papers

# FIGURE 15. Topics in the Secure Software Testing Stage.

# TABLE 18. Topics in the Secure Software Testing Stage.

Issues are detecting vulnerabilities and exploit vulnerabilities prevention.

We also reviewed 57 articles to identify standards of vulnerabilities; the results appear in Figure 14 and Table 17. The National Vulnerability Database (NVD) and the Common Vulnerabilities and Exposures (CVE) are the ones that appeared most in the studies. Another noteworthy fact is that the vulnerability reports show that the vulnerabilities are related to common mistakes that are made during the programming phase [24].

# E. RQ5: WHAT TECHNIQUES ARE PREVALENT AT SOFTWARE TESTING SECURITY?

Software security tests verify that the software protects data and complies with the implementation of the Software security requirements. There is a diversity of techniques and tools in the software security testing stage, among which the most notable are vulnerability scanning, penetration tests, risk assessment, security audit, ethical hacking, posture assessment, and safety regression [30]–[33]. The present study identified 83 papers related to software testing security; Figure 15 and Table 18 summarizes the findings.

# IV. CONCLUSION AND FUTURE WORK

Unauthorized access to confidential data is frequent, and security threats grow exponentially. Hence the importance of developing secure software. However, in the literature it has been reported that secure software development approaches have weaknesses or are little or not accessible for their use in the software industry.

To deepen into these issues, this study provides an overview of trends in secure software development by reviewing 528 articles. We found out that the most frequently reported topics are software construction security or secure coding, evaluation research in security, case study papers, vulnerabilities in web applications, need for assistance and training in security for developers, and proposal of new security software models. The topics less frequently reported are.

VOLUME 9, 2021

36865

# H. Nina et al.: Systematic Mapping of the Literature on Secure Software Development

security principles, agile techniques and methods, popular secure software development models (OWASP or Microsoft SDL), and artificial intelligence techniques. Specifically,

in the security requirements stage, the most frequently reported are elicitation and analysis of security requirements and the Misuse case technique. Recurring themes in secure software design are security in component-based software development, threat modeling, and security patterns. The secure code construction stage reported most frequently to static code analysis, vulnerability detection, and public vulnerability database (NVD). In the software security testing stage, vulnerability scanning and penetration testing are the most recurrent topics.

Finally, to know the characteristics of a secure software development method, technique, or tool, it is necessary to deepen the study by conducting systematic reviews.

# APPENDIX

# Papers Identified in the Systematic mapping of the literature on Secure Software Development

This information is available at: http://inform.pucp.edu.pe/~jpowsang/ssd/mapping_study_appendix.htm

# REFERENCES

1. E. Bodden, ‘‘State of the systems security,’’ in Proc. IEEE/ACM 40th Int. Conf. Softw. Eng., Companion (ICSE-Companion), May 2018, pp. 550–551.
2. X. Meng, K. Qian, D. Lo, H. Shahriar, M. A. I. Talukder, and P. Bhattacharya, ‘‘Secure mobile IPC software development with vulnerability detectors in Android studio,’’ in Proc. IEEE 42nd Annu. Comput. Softw. Appl. Conf. (COMPSAC), Jul. 2018, pp. 829–830, doi: 10.1109/COMPSAC.2018.00141.
3. R. A. Khan and S. U. Khan, ‘‘A preliminary structure of software security assurance model,’’ in Proc. 13th Int. Conf. Global Softw. Eng., May 2018, pp. 132–135.
4. M. Saito, A. Hazeyama, N. Yoshioka, T. Kobashi, H. Washizaki, H. Kaiya, and T. Ohkubo, ‘‘A case-based management system for secure software development using software security knowledge,’’ Procedia Comput. Sci., vol. 60, pp. 1092–1100, Jan. 2015.
5. M. Busch, N. Koch, and M. Wirsing, ‘‘Evaluation of engineering approaches in the secure software development life cycle,’’ in Engineering Secure Future Internet Services and Systems (Lecture Notes in Computer Science), vol. 8431, M. Heisel, W. Joosen, J. Lopez, and F. Martinelli, Eds. Cham, Switzerland: Springer, 2014, doi: 10.1007/978-3-319-07452-8_10.
6. M. Ramachandran, ‘‘Software security requirements engineering: State of the art,’’ in Proc. Int. Conf. Global Secur., Saf., Sustainability, 2015, pp. 313–322.
7. M. Felderer, B. Katt, P. Kalb, J. Jürjens, M. Ochoa, F. Paci, T. T. Tun, K. Yskout, R. Scandariato, F. Piessens, ‘‘Evolution of security engineering artifacts: A state of the art survey,’’ Int. J. Secure Softw. Eng. IJSSE, vol. 5, no. 4, pp. 48–98, 2014.
8. H. Villamizar, M. Kalinowski, M. Viana, and D. M. Fernandez, ‘‘A systematic mapping study on security in agile requirements engineering,’’ in Proc. 44th Euromicro Conf. Softw. Eng. Adv. Appl. (SEAA), Aug. 2018, pp. 454–461.
9. A. Souag, R. Mazo, C. Salinesi, and I. Comyn-Wattiau, ‘‘Reusable knowledge in security requirements engineering: A systematic mapping study,’’ Requirements Eng., vol. 21, no. 2, pp. 251–283, Jun. 2016.
10. P. H. Nguyen, S. Ali, and T. Yue, ‘‘Model-based security engineering for cyber-physical systems: A systematic mapping study,’’ Inf. Softw. Technol., vol. 83, pp. 116–135, Mar. 2017.
11. S. Rehman, V. Gruhn, S. Shafiq, and Y. I. Inayat, ‘‘A systematic mapping study on security requirements engineering frameworks for cyber-physical systems,’’ in Proc. Int. Conf. Secur., Privacy Anonymity Comput., Commun. Storage, Dec. 2018, pp. 428–442.
12. P. Silva, R. Noël, M. Gallego, S. Matalonga, and Y. H. Astudillo, ‘‘Software development initiatives to identify and mitigate security threats: A systematic mapping,’’ in Proc. CIbSE, 2016, pp. 257–270.
13. S. Wu, C. Zhang, and F. Wang, ‘‘Extracting software security concerns of problem frames based on a mapping study,’’ in Proc. 24th Asia–Pacific Softw. Eng. Conf. Workshops (APSECW), Dec. 2017, pp. 121–125.
14. N. M. Mohammed, M. Niazi, M. Alshayeb, and S. Mahmood, ‘‘Exploring software security approaches in software development lifecycle: A systematic mapping study,’’ Comput. Standards Interface, vol. 50, pp. 107–115, Feb. 2017.
15. B. Kitchenham and S. Charters, ‘‘Guidelines for performing systematic literature reviews in software engineering,’’ Keele Univ., Keele, U.K., Durham Univ., Durham, U.K., Tech. Rep., 2007.
16. M. Felderer and J. C. Carver, ‘‘Guidelines for systematic mapping studies in security engineering,’’ in Empirical Research for Software Security. Boca Raton, FL, USA: CRC Press, 2017, pp. 47–68.
17. C. Lockwood, Z. Munn, and K. Porritt, ‘‘Qualitative research synthesis: Methodological guidance for systematic reviewers utilizing meta-aggregation,’’ Int. J. Evidence-Based Healthcare, vol. 13, no. 3, pp. 179–187, 2015.
18. M. Petticrew and H. Roberts, Systematic Reviews in the Social Sciences: A Practical Guide. Hoboken, NJ, USA: Wiley, 2008.
19. I. C. Society, P. Bourque, and R. E. Fairley, Guide to the Software Engineering Body of Knowledge (SWEBOK(R)): Version 3.0, 3rd ed. Los Alamitos, CA, USA: IEEE Computer Society Press, 2014.
20. W. A. Conklin and D. Shoemaker, CSSLP Certification All-in-One Exam Guide, 2nd ed. New York, NY, USA: McGraw-Hill, 2019.
21. J. C. Carver, M. Burcham, S. A. Kocak, A. Bener, M. Felderer, M. Gander, J. King, J. Markkula, M. Oivo, C. Sauerwein, and L. Williams, ‘‘Establishing a baseline for measuring advancement in the science of security: An analysis of the 2015 IEEE security & privacy proceedings,’’ in Proc. Symp. Bootcamp Sci. Secur., Apr. 2016, pp. 38–51.
22. L. Siddique and B. A. Hussein, ‘‘Practical insight about choice of methodology in large complex software projects in Norway,’’ in Proc. IEEE Int. Technol. Manage. Conf., Jun. 2014, pp. 1–4, doi: 10.1109/ITMC.2014.6918615.
23. D. Oliveira, M. Rosenthal, N. Morin, K.-C. Yeh, J. Cappos, and Y. Zhuang, ‘‘It’s the psychology stupid: How heuristics explain software vulnerabilities and how priming can illuminate developer’s blind spots,’’ in Proc. 30th Annu. Comput. Secur. Appl. Conf. ACSAC, 2014, pp. 296–305.
24. T. Lopez, H. Sharp, T. Tun, A. Bandara, M. Levine, and B. Nuseibeh, ‘‘‘Hopefully we are mostly secure’: Views on secure code in professional practice,’’ in Proc. IEEE/ACM 12th Int. Workshop Cooperat. Hum. Aspects Softw. Eng. (CHASE), May 2019, pp. 61–68, doi: 10.1109/CHASE.2019.00023.
25. T. Winograd, H. L. McKinley, L. Oh, M. Colon, T. McGibbon, E. Fedchak, and R. Vienneau, Software Security Assurance: A State-of-the Art Report (SOAR). Herndon, VA, USA: Information Assurance Technology Analysis Center (IATAC) Data and Analysis Center for Software (DACS), 2007.
26. S. Simpson, ‘‘SAFECode whitepaper: Fundamental practices for secure software development 2nd edition,’’ in Proc. ISSE Securing Electronic Business Processes, Wiesbaden, Germany, 2014, pp. 1–32.
27. E. Rodriguez, ‘‘Security design patterns,’’ in Proc. 19th Annu. Comput. Secur. Appl. Conf. (ACSAC), 2003.
28. A. V. Uzunov, E. B. Fernandez, and K. Falkner, ‘‘Securing distributed systems using patterns: A survey,’’ Comput. Secur., vol. 31, no. 5, pp. 681–703, Jul. 2012.
29. S. Barnum and A. Sethi, ‘‘Attack patterns as a knowledge resource for building secure software,’’ in Proc. OMG Softw. Assurance Workshop, Cigital, 2007.
30. Y.-H. Tung, S.-C. Lo, J.-F. Shih, and H.-F. Lin, ‘‘An integrated security testing framework for secure software development life cycle,’’ in Proc. 18th Asia–Pacific Netw. Oper. Manage. Symp. (APNOMS), Oct. 2016, pp. 1–4.
31. V. V. Ribeiro, D. S. Cruzes, and G. H. Travassos, ‘‘A perception of the practice of software security and performance verification,’’ in Proc. 25th Australas. Softw. Eng. Conf. (ASWEC), Nov. 2018, pp. 71–80.
32. P. Nidagundi and M. Uhanova, ‘‘Software application security test strategy with lean canvas design,’’ in Proc. IVUS Int. Conf. Inf. Technol., Kaunas, Lithuania, Apr. 2018.
33. M. Felderer, M. Büchler, M. Johns, A. D. Brucker, R. Breu, and Y. A. Pretschner, ‘‘Security testing: A survey,’’ in Advances in Computers, vol. 101. Amsterdam, The Netherlands: Elsevier, 2016, pp. 1–51.

# H. Nina et al.: Systematic Mapping of the Literature on Secure Software Development

# HERNAN NINA

(Senior Member, IEEE) received the B.Sc. degree in informatics and system engineering and the Master of Administration degree from the Universidad Nacional de San Antonio Abad del Cusco (UNSAAC), Peru, the master’s degree in informatica with mention in software engineering from the Pontificia Universidad Católica del Perú (PUCP), and the Ph.D. degree in system engineering from Universidad Nacional Federico Villareal (UNFV), Peru. He was qualified as a Researcher from CONCYTEC, Peru. He is currently a Full Professor with the Universidad de Lima, Peru. His research interests include software engineering, innovation in higher education, and human–computer interaction. He is also a member of ACM. He has published several articles in the field of effort estimation for software development projects. His research interests include empirical software engineering, software metrics, software engineering education, and human–computer interaction. He is a member of ACM and the IEEE Computer Society. He has been elected President of the Peruvian Section of the IEEE Computer Society from 2015 to 2018.

# JOSÉ ANTONIO POW-SANG

(Senior Member, IEEE) received the B.Sc. degree in informatics engineering and the Licentiate degree in education for development from the Pontificia Universidad Católica del Perú (PUCP), and the master’s degree in software engineering and the Ph.D. degree in informatics engineering from the Universidad Politécnica de Madrid, Spain. He was the Executive Director of the Postgraduate School from 2013 to 2020 and the Director of the Master’s Program in Informatics from 2011 to 2020. He is currently a Full Professor.

# MÓNICA VILLAVICENCIO

received the Ph.D. degree in applied engineering from the École de technologie Súperieure, UQAM, Montreal, QC, Canada. She is currently a Full Professor with the Faculty of Electrical and Computer Engineering, Escuela Superior Politécnica del Litoral (ESPOL), Ecuador, where she teaches software engineering-related courses to undergraduate and graduate students. She is also the Director of the Doctorate Program of Applied Computer Science, ESPOL. Her research interests include agile software development, software measurement, software engineering education, and applied software engineering to the IoT and intelligent systems.

VOLUME 9, 2021 36867