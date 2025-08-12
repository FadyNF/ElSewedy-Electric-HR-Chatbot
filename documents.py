document_forms = [
    # Form 1: Car Allowance Agreement Form
    """
    ELSEWEDY ELECTRIC

    Car Allowance Agreement Form

    This agreement is dated on ________________________

    Employee Details:

    Employee Name
    Employee Universal ID
    Position Name
    Employee Grade
    Department
    Line Manager Name
    Line Manager Position Title
    Car Allowance in EGP

    It is hereby agreed and declared that, in accordance to car allowance policy issued in 2024, payback rule will be applied on the following cases:

    - The employee who will leave within 5 years following the car allowance delivery date, he/she needs to pay back the remaining amount of the received allowance pro-rata in cash or to be deducted from his financial dues at the end of his service.

    Approvals/ Signatures:

    Name                          Signature
    Employee
    Name: _________________

    BU Head
    Name: _________________

    Finance Department Head
    Name: __________________
    """,

    # Form 2: Arabic Exceptional Advance Request Form
    """
    ELSEWEDY ELECTRIC

    طلب سلفة استثنائية

    اسم الموظف:                    الوظيفة:

    الكود الوظيفي:        مبلغ السلفة :        عدد أشهر التقسيط:

    سبب السلفة بالتفصيل:
    -الزواج (الموظف أو الأبناء).
    -الكوارث (الحريق – الزلازل –انهيار المنازل –الحوادث).
    -الحج.

    توقيع الموظف :                    التاريخ:

    اسم الضامن الأول :        رقم الكود:        التوقيع:

    اسم الضامن الثاني:        رقم الكود:        التوقيع:

    اسم المدير المباشر:        رقم الكود:        التوقيع:

    مبلغ السلفة الذي تم الموافقة عليه:        عدد أشهر التقسيط:        توقيع مدير الموارد البشرية:

    توقيع مدير عام الشركة
    """,

    # Form 3: Arabic Advance Request Form
    """
    ELSEWEDY ELECTRIC

    طلب سلفة

    اسم الموظف:                    الوظيفة:

    الكود الوظيفي:        مبلغ السلفة :        عدد أشهر التقسيط:

    توقيع الموظف :                    التاريخ:

    اسم الضامن الأول :        رقم الكود:        التوقيع:

    اسم الضامن الثاني:        رقم الكود:        التوقيع:

    اسم المدير المباشر:        رقم الكود:        التوقيع:

    مبلغ السلفة الذي تم الموافقة عليه:        عدد أشهر التقسيط:        توقيع مدير الموارد البشرية:

    توقيع مدير عام الشركة
    """,

    # Form 4: Loan Request Form
    """
    ELSEWEDY ELECTRIC

    Loan request

    Employee Name:                    Job title:

    Employee oracle Code:        Loan amount:        Installments months:

    Employee signature:                    Date:

    First guarantor name:        oracle Code:        Signature:

    Second guarantor name:        oracle Code:        Signature:

    Direct manager name:        oracle Code:        Signature:

    Approved loan amount        Installments months:        HRBP signature:

    GM/MD/CEO signature
    """,

    # Form 5: Exceptional Loan Request Form
    """
    ELSEWEDY ELECTRIC

    Exceptional Loan request

    Employee Name:                    Job title:

    Employee oracle Code:        Loan amount:        Installments months:

    The detailed reason for the loan:

    -Marriage (self / children).

    - Disasters (Fire - earthquakes - house collapses - accidents).

    - Haj.

    Employee signature:                    Date:

    First guarantor name:        oracle Code:        Signature:

    Second guarantor name:        oracle Code:        Signature:

    Direct manager name:        oracle Code:        Signature:

    Approved loan amount        Installments months:        HRBP signature:

    GM/MD/CEO signature
    """
]

meta_forms= [{
        "form_id":"car_allowance_agreement_form",
        "form_name":"Car Allowance Agreement Form",
        "form_name_ar":"نموذج اتفاقية بدل السيارة",
        "description":"Agreement form for car allowance with 5-year payback terms and employee details",
        "description_ar":"نموذج اتفاقية بدل السيارة مع شروط الاسترداد لمدة 5 سنوات وتفاصيل الموظف",
        "file_path":"data/forms/Car Allowance Agreement Form.pdf",
        "related_policies":"car_allowance_policy_2024",
        "keywords":["car", "allowance", "agreement", "payback", "employee", "5-year", "EGP", "signature"]
    },
            # Image 1: Arabic Exceptional Loan Request
        {
            "form_id":"arabic_exceptional_loan_request_form",
            "form_name":"Arabic Exceptional Loan Request Form",
            "form_name_ar":"نموذج طلب سلفة استثنائية",
            "description":"Arabic form for exceptional loan requests including marriage, disasters, and Hajj purposes",
            "description_ar":"النموذج العربي لطلب السلف الاستثنائية بما في ذلك الزواج والكوارث والحج",
            "file_path":"data/forms/Arabic Exceptional Loan Request.jpg",
            "related_policies":"exceptional_loans_policy",
            "keywords":["exceptional", "loan", "arabic", "marriage", "disasters", "hajj", "guarantor", "installments"]
        },

        # Image 2: Arabic Regular Loan Request
        {
            "form_id":"arabic_regular_loan_request_form",
            "form_name":"Arabic Regular Loan Request Form",
            "form_name_ar":"نموذج طلب سلفة",
            "description":"Standard Arabic form for regular employee loan requests",
            "description_ar":"النموذج العربي القياسي لطلب سلف الموظفين العادية",
            "file_path":"data/forms/Arabic Regular Loan Request.jpg",
            "related_policies":"employee_loans_policy, loan_approval_policy",
            "keywords":["loan", "arabic", "employee", "installments", "guarantor", "signature"]
        },
        # Image 3: English Regular Loan Request
        {
            "form_id":"english_regular_loan_request_form",
            "form_name":"English Regular Loan Request Form",
            "form_name_ar":"نموذج طلب السلفة باللغة الإنجليزية",
            "description":"Standard English form for regular employee loan requests with HRBP and executive approval",
            "description_ar":"النموذج الإنجليزي القياسي لطلب سلف الموظفين مع موافقة الموارد البشرية والإدارة التنفيذية",
            "file_path":"data/forms/English Regular Loan Request.jpg",
            "related_policies":"employee_loans_policy, loan_approval_policy",
            "keywords":["loan", "english", "employee", "oracle", "HRBP", "GM", "MD", "CEO", "guarantor"]
        },

        # Image 4: English Exceptional Loan Request
        {
            "form_id":"english_exceptional_loan_request_form",
            "form_name":"English Exceptional Loan Request Form",
            "form_name_ar":"نموذج طلب السلفة الاستثنائية باللغة الإنجليزية",
            "description":"English form for exceptional loan requests covering marriage, disasters, and Hajj with executive approval required",
            "description_ar":"النموذج الإنجليزي لطلب السلف الاستثنائية للزواج والكوارث والحج مع اشتراط الموافقة التنفيذية",
            "file_path":"data/forms/English Exceptional Loan Request.jpg",
            "related_policies":"exceptional_loans_policy",
            "keywords":["exceptional", "loan", "english", "marriage", "disasters", "hajj", "oracle", "HRBP", "GM", "MD", "CEO"]
        },

        ]

# ---------------------------------

documents = [
    [
    {"section": "Policy Overview",
    "content": """Employees Loans Policy

    Aim: To set a standard system for employees' loans in El Sewedy Electric Group as the group aims at alleviating the employees' burdens in emergency cases.

    Scope: El Sewedy Electric companies in Egypt.

    Responsible Employees:
    - GM.
    - Finance Managers.
    - HR Managers.
    - Dept. Managers.

    Definitions: None."""},

    {"section": "General Principles - Eligibility and Basic Terms",
    "content": """General Principles:

    An employee who spent a full year in service is entitled to make a request for a maximum of three months' salary loan to be repaid in monthly installments by the end of one year and half.

    A year must pass after the last paid installment of the loan given to the employee, and two guarantors who have been in service for over two years or more for each must sign the request.

    One guarantor can grant a maximum of 2 employees.

    The guarantors will repay the loan in the case that the employee is unable to pay it."""},

    {"section": "Loan Limits and Termination Policy",
    "content": """In case of termination of the employee's contract for any reason, the amount of the loan shall be deducted at once.

    All approved loans balance shouldn't exceed 25% of the company's total monthly salaries and should be in accordance with its financial position.

    Any exceptions from this policy shall be approved by the BU GM/MD/CEO"""},

    {"section": "Application Procedures",
    "content": """Procedures:

    An employee must fill out a loan request form specifying the required amount not exceeding three months' salary. The form must include the signatures of the two guarantors.

    An employee must submit the form to his/her direct manager for approval, being sure of the guarantors' signatures.

    An employee must submit the form to HR Dept. for revision in accordance with the above-mentioned terms and conditions after his or her direct manager's approval."""},

    {"section": "Processing and Payment",
    "content": """Then the loans are approved and grouped into one statement, the loans balance shouldn't exceed 25% of the company's total monthly salaries.

    HR Dept. shall coordinate with Finance to provide the required amount of loan, hand it over to the employee, and deduct the monthly installments from his/her next salary over a maximum period of 18 months."""},

    {"section": "Documentation and Exemptions",
    "content": """Required documents:
    A loan request with the signatures of the employee, guarantors, and direct manager stating the amount of the requested loan.

    Exemption:
    The exemption is made in the case of death or total disability.

    Used Forms:
    Attached."""}
],

 [
    {"section": "Policy Title and Overview",
    "content": """سياسة سلف العاملين

    الهدف: وضع نظام موحد لسلف العاملين بمجموعة شركات السويدي الكتريك حيث تهدف المجموعة إلى المشاركة في تخفيف العبء عن العاملين في الظروف الطارئة.

    نطاق التطبيق: شركات السويدي الكتريك داخل جمهورية مصر العربية.

    المسئولين:
    - مدير عام الشركة.
    - المديرين الماليين.
    - مديري الموارد البشرية
    - مديري الإدارات.

    التعريفات: لا يوجد."""},

    {"section": "General Principles",
    "content": """المبادئ العامة:

    للموظف الذي أمضى في الخدمة عاما كاملا الحق في طلب سلفة من الشركة لمواجهة الظروف الطارئة بحد أقصى ثلاثة أشهر من إجمالي الراتب وتسدد على أقساط شهرية بحد أقصى سنة ونصف ميلادية.

    يشترط مرور عام على آخر قسط للأجل كما يشترط وجود عدد 2 ضامن من على خدمة كل منهما متزة عامان أو أكثر.

    يستطيع الضامن الواحد أن يضمن 2 موظفين بحد أقصى.

    في حالة عجز الموظف عن سداد السلفة سيقوم الضامنين بسداد السلفة بدلا عنه.

    في حالة إنهاء خدمة الموظف لأي سبب من الأسباب يتم خصم مبلغ السلفة دفعة واحدة."""},

    {"section": "Financial Limits and Procedures",
    "content": """إجمالي رصيد السلف التي يتم اعتمادها يجب ألا يتجاوز 25% من إجمالي مرتبات الشركة الشهرية ويما يتوافق مع موقفها المالي.

    أي استثناءات عن هذه السياسة يتم اعتمادها من المدير العام للشركة.

    الإجراءات:

    يقوم الموظف بتحرير نموذج طلب السلفة محددا فيه المبلغ المطلوب بحيث لا يتجاوز راتب ثلاثة شهور، ويتضمن النموذج توقيع ضامنتين.

    يقوم الموظف بتقديم الطلب إلى المدير المباشر لاعتماده والتأكد من توقيع الضامنين.

    يقوم الموظف بعد اعتماد المدير المباشر بتقديم الطلب لإدارة الموارد البشرية التي تقوم بمراجعة الطلب طبقا للشروط السابقة."""},

    {"section": "Final Processing",
    "content": """ثم يتم اعتماد السلف مجمعة في بيان واحد، على ألا يتجاوز إجمالي رصيد السلف 25% من إجمالي المرتبات شهريا.

    تقوم إدارة الموارد البشرية بالتنسيق مع الإدارة المالية لصرف مبلغ السلفة وتسليمه للموظف ويقوم بخصم الأقساط الشهرية من راتب الموظف من الشهر التالي لصرف بحد أقصى 18 شهرا.

    الأوراق المطلوبة:
    طلب السلفة مع إمضاء الموظف والضامنتين والمدير المباشر موضح به مبلغ السلفة المطلوبة.

    الإعفاء:
    يتم الإعفاء في حالة الوفاة أو العجز الكلي لا قدر الله.

    النماذج المستخدمة:
    مرفق."""}
],

    [
    {"section": "Definition and Overview",
    "content": """Internal Job Posting Criteria - Definitions
    Internal Job Posting is a process that advertises job openings to current employees before posting it externally."""},

    {"section": "Pre-requisites from BU/Sector/Country HRBP",
    "content": """Pre-requisites needed from the BU/Sector/Country HRBP before initiating the requisition to Group Internal Mobility:
    1. Available job at the requested grade based on the approved structure from Group OD prior the communication with the Group Internal Mobility
    2. Available JD in the Group unified template approved from Group OD.
    3. Confirmation mail from Group OD on the JD that includes position title, grade, qualifications, reporting line, and accountabilities."""},

    {"section": "Requisition Process",
    "content": """Requisition Process:
    1. The Sector/Country/BU HRBP notifies the Group Internal Mobility Group.im@elsewedy.com of any job openings based on the criteria mentioned above and copy the confirmation mail from Group OD.
    2. The Group Internal Mobility validates the request against the approved manpower plan.
    3. The Group Internal Mobility sends an email to all employees across the group via Group.im@elsewedy.com mentioning the open position, the job description, and the required qualifications."""},

    {"section": "Application Criteria",
    "content": """Criteria for applying:
    ✓ New hires should have spent at least 12 months in the current role at Elsewedy Electric.
    ✓ Candidate should be identified as a (key talent), (watch-lister) or (high potential) employee.
    ✓ Recently promoted employees must spend a minimum period before applying for a higher-level (vertical) transfer:
    • Same band: Employees must have at least 6 months in their current role.
    • Higher band: Employees must have at least 12 months in their current role."""},

    {"section": "Application Process",
    "content": """Application Process:
    • The Employee to send his/her CV to Group.im@elsewedy.com replying to the job post copying his/her HRBP.
    • Once the application is approved, the Employee will be interviewed by the job owner.
    • The handover period will be from 10-20 working days before the internal transfer takes place."""},

    {"section": "General Rules and Policies",
    "content": """General Rules:
    • Hiring Managers who want an employee to join their team can only reach out to the employee's current line manager & BU HRBP.
    • Internal Transfers do not necessitate a pay increase and the Sector/BU HRBP to make sure not to exceed the personnel cost versus the sales revenue ratio budget set for the year.
    • The employee can be transferred to a higher band considering his TAC results that must be conducted prior granting the upgraded job level.
    • Employees who violate the Process, will be given a verbal warning and will be disqualified from consideration and receive a warning letter, which may be reflected in their performance appraisal, bonus, or promotion.
    • Employees/Hiring Managers who violate the process and hunt or poach internal talents from other internal Business Units will be subject to disciplinary action."""
}],

    [
    {"section": "Purpose",
    "content": """Purpose: To outline the guidelines and process for the transfer of employees to a new role within the group, ensuring that the employees utilize their skills in different areas and retain them by providing growth opportunities. This approach encourages internal mobility and career development within the Group while considering the cultural fit of the candidates, as internal employees are already familiar with the company culture and values, which can lead to smoother transitions. This Policy is a minimum standard; where local legislations define higher standards; the Group shall comply with them.""",},

    {"section": "Applicability",
    "content": """Applicability: This policy applies to all the operating companies and subsidiaries directly or indirectly controlled by Elsewedy Electric, and all the geographical regions where Elsewedy Electric companies and subsidiaries are operating.""",},

    {"section": "Definitions - Internal Mobility Types",
    "content": """Definitions - Internal Mobility: Internal Mobility is the process of transferring an employee to a new role in another Function, Department or Business Unit in the same country within the Group, and there are 2 types of transfer: Lateral Transfer is moving an employee to a different role at the same level (grade) within the Group. Vertical Transfer is moving an employee to a higher level (grade or band) position within the Group.""",},

    {"section": "Definitions - Other Key Terms",
    "content": """Definitions - Additional Terms: Internal Job Posting is a process that advertises job openings to current employees before posting it externally. No Poach is an agreement not to hunt, recruit employees from other Business Units within the Group or from external companies that we have agreement with to avoid active headhunting talents from. Talent Assessment Center (TAC) is assessing Elsewedy Competency model (Core & Leadership) through behavioral business simulations that reflect the employees' competency level based on pre-agreed behavior indicators/level.""",},

    {"section": "Internal Mobility Process Steps 1-4",
    "content": """The Internal Mobility Process Steps 1-4: 1. The Sector/Country/BU HRBP notifies the Group Internal Mobility of any job openings based on the following criteria: Approved organization structure. The organization structure, to be approved by the Group Organization Design Team prior the communication with the Talent Acquisition Team. Available job at the requested grade. The jobs to be evaluated by the Group Total Rewards Team. Confirmation mail from Group OD on the JD that includes position title, grade, qualifications, reporting line, and accountabilities. 2. Group Internal Mobility validates the request against the approved manpower plan and sends an email to all employees across the group via Group.im@elsewedy.com that includes the unified internal job posting template. 3. Employees who are interested in the job posts in another Business Unit within the Group must apply through Group.im@elsewedy.com, copying the HRBP of the Business Unit. 4. Group Internal Mobility reviews all applications to ensure they meet the required criteria and share the qualified applications with the hiring manager.""",},

    {"section": "Internal Mobility Process Steps 5-9",
    "content": """The Internal Mobility Process Steps 5-9: 5. The hiring manager interviews the shortlisted employees. 6. TAC to be conducted for vertical transfers to a higher band. 7. Group Internal Mobility works closely with the Group Total Rewards to create an offer for the selected employee. 8. The selected employee grants the position and the other applicants are informed about the status of their application. 9. Group Internal Mobility aligns the start date of the selected employee with the Sector/Country/BU HRBP and the employee with a handover period of 10-20 working days before the internal transfer takes place.""",},

    {"section": "Basic Principles - Restrictions and Requirements",
    "content": """Basic Principles - Key Restrictions: It's crucial not to approach or promise any of the colleagues in other departments or Business Units for a move from his current role. Hiring Managers who wish for an employee to join their teams, their only channel is to reach out to his current line manager & BU HRBP only. New hires should have spent at least 6 months in the current role at Elsewedy Electric. Recently promoted employees must spend a minimum period before applying for a vertical transfer: Vertical transfer within the same band: Employees must have at least 6 months in their current role. Vertical transfer to a higher band: Employees must have at least 12 months in their current role.""",},

    {"section": "Basic Principles - Additional Requirements",
    "content": """Basic Principles - Additional Requirements: Internal Transfers do not necessitate a pay increase and the Sector/BU HRBP to make sure not to exceed the personnel cost versus the sales revenue ratio budget set for the year. The employee can be transferred to a higher band considering his TAC results that must be conducted prior granting the upgraded job level. Employees should be identified as a (key talent), (watch-lister) or (high potential). If an employee declines an offer, their decision will not affect their current job.""",},

    {"section": "Disciplinary Action",
    "content": """Disciplinary Action: In case the employee's direct manager didn't approve his transfer, the employee may escalate to his BU HRBP and department head to take actions accordingly. Employees who do not abide by the transfer guidelines will be disqualified from consideration. Employees/Hiring Managers who violate the policy and hunt or poach internal talents will be given a verbal warning and will receive a warning letter, which may be reflected in their performance appraisal, bonus, or promotion.""",},

    {"section":" Policy Compliance",
    "content": """Policy Compliance: Elsewedy Electric may conduct regular audits in all its facilities and structures to monitor compliance with this policy. The Group could also conduct internal surveys or initiatives to encourage the employees to always report violations of its policies. All concerns related to the policy shall be freely raised and appropriately handled and followed up by the Group. All Elsewedy Electric staff members are expected to report any case of non-compliance with the policy. The employees should be aware that they have a moral and ethical duty to report such instances and should not fear retaliation. The Group recognizes the importance of confidentiality and could grant anonymity to the complainants who wish so, given that such information does not impede the investigation or resolution of the dispute. There should be no limitation to the filing of complaints, in terms of accessibility to all employees and quantity. The Group will make sure that the employees know where and to whom they can refer for denounces or complaints. Elsewedy Electric ensures that appropriate measures and penalties will be applied in case of non-compliance with this policy.""",},

    {"section":" Discipline & Remediation",
    "content": """Discipline & Remediation: Violations of this policy may lead to disciplinary action up to, and including, termination of employment/partnership. All disciplinary actions shall be undertaken in accordance with the Group's sanctions list and with all applicable local laws and other legal requirements. The remediation shall be undertaken on a case-by-case basis and in accordance with all applicable local laws and other legal requirements.""",},

    {"section":" Policy Review",
    "content": """Policy Review: This policy shall be reviewed annually and/or when deemed necessary."""}
],

[
    {
        "chunk_id": 1,
        "section": "Performance Culture Introduction",
        "content": "Our commitment to building and sustaining a Performance Culture essentially means that we focus on improving the results at our organization by hiring, developing, and retaining high performers (employees who are capable, engaged, and performing). Performance Management is the foundation of performance excellence in the organization and therefore, we are glad to kick-off our performance appraisal cycle."
    },
    {
        "chunk_id": 2,
        "section": "Past Year Survey Results Summary",
        "content": "Past Year, Performance Appraisal Quality Survey shows overall response rate of 45% (2,712 responses out of 6,041 invited). Satisfaction rates: Non-Managers 78%, Managers+ 78%. Response rates varied by sector: WC&A 44%, Electrical Products 45%, Iskraemeco 40%, E&C 54%, Infra Sector 53%, Digital 26%, Educational 71%, IBP 26%, Corporate 37%, Algeria 1%, East Africa 0%, KSA 7%, Qatar 40%, Kuwait 0%, Electric UAE 33%."
    },
    {
        "chunk_id": 3,
        "section": "Mid-Year Reviews Implementation",
        "content": "Annual goals might have worked 20 years ago, but between new technologies and a rapidly changing economy it is hard for goals to be relevant for all year. In 2025, we aim to conduct a Mid-Year review during June-July, to follow up with business units to assess their adherence to the set goals and milestones, in addition to any support they need from our side to stay on the right track. This collaborative review process will help us ensure that we are collectively moving to the right direction and making necessary adjustments as needed. A (Mid-year Review Quality Survey) will be introduced in 2025."
    },
    {
        "chunk_id": 4,
        "section": "Performance Appraisal Components",
        "content": "The evaluation of the employee is determined based on 4 components: 1. Goals' achievements: a. Business Goals' achievement, b. Individual Goals achievement. 2. Behaviors demonstrated: a. Core Competencies (for all Bands), b. Leadership Competencies (for Senior Professionals Band and above)."
    },
    {
        "chunk_id": 5,
        "section": "Business Goals Achievement Framework",
        "content": "Reaching the business goals set in the beginning of the year using the Balanced Scorecard (BSC) methodology based on the 4 perspectives: 1. The Financials 2. The Customers 3. The Internal Processes 4. The People (learning and growth). Each business has selected a set of goals to work on during the past year and cascaded these goals to the departments and individuals."
    },
    {
        "chunk_id": 6,
        "section": "Business Performance Calculation Evolution",
        "content": "PA 2022: 85% Financials (F1-F5), 5% Customers (Mar), 5% Processes (IT), 5% People (HR). PA 2023: 100% Financials (F1-F2). PA 2024: 70% Financial (F1-F5), 10% Customers (Marketing), 10% Processes (IT), 10% People (HR)."
    },
    {
        "chunk_id": 7,
        "section": "2024 Business Results Calculation Process",
        "content": "For this year PA 2024, The Financials' Perspective results will be discussed and decided between by the Group CFO and the Sector/Countries CEOs, CFOs and HRBPs. The People's Perspective results will be discussed and decided between by the Group CHRO and the Sector/Countries CEOs and HRBPs. Starting next year, the PA 2025, The Customers' Perspective goals and results will be discussed and agreed between the Group CRM team and the Sector/Countries CEOs, CFOs and HRBPs. The Processes' Perspective goals and results between the Group Audit and Group IT teams and the Sector/Countries Heads, CFOs and HRBPs."
    },
    {
        "chunk_id": 8,
        "section": "Performance Appraisal Calculation Table by Band",
        "content": "Leadership Band: 30% Business Goals Achievement, 80% Individual Goals Achievement, 20% Core & Leadership Competencies. Senior Management Band: 40% Business Goals Achievement, 40% Individual Goals Achievement, 20% Core & Leadership Competencies. Management Band: 60% Individual Goals Achievement, 20% Business Goals Achievement, 20% Core & Leadership Competencies. Senior Professionals Band: 80% Individual Goals Achievement, 20% Core Competencies. Professionals Band: 80% Individual Goals Achievement, 20% Core Competencies."
    },
    {
        "chunk_id": 9,
        "section": "Individual Goals Achievement Definition",
        "content": "Reaching specific, desirable goals that were agreed in the beginning of the year with the line manager as part of the company's overall goals. The total percentage of the individual's goals is 100% and their weight in the performance appraisal is marked in the table above as per the individual's job band."
    },
    {
        "chunk_id": 10,
        "section": "Core Behaviors and Leadership Competencies",
        "content": "Core Behaviours: Accountability & Responsibility, Effective Communication, Cooperation & Collaboration, Customer Focus, Excellence in Execution. Competencies of Leadership: Business Acumen, Building Teams, Developing & Retaining Talent, Managing Change, Global Mindset. The new Group Competency Model will be launched in February 2025."
    },
    {
        "chunk_id": 11,
        "section": "Performance Appraisal Rating Scale",
        "content": "Our rating is designed on 5-point rating scale to help reduce bias and allow for more accurate evaluation. Please! Anything that is above 3 requires extra work and overachieving the goal. You must justify it if you give an employee a 4 or 5, and you must put the employee in a performance improvement plan (PIP) if you rank them 2 or 1. Rating Scale: Unsatisfactory <80%, Needs Improvement 80%-89%, Meets Expectations 90%-105%, Exceeds Expectations 106%-120%, Significantly Exceeds Expectations >120% (cap to 140%)."
    },
    {
        "chunk_id": 12,
        "section": "Development Plan and Career Ambition",
        "content": "At the end of the PA, it is critical to discuss: 1. The employee's strengths and areas of development, 2. His/her career aspiration, and 3. His/her improvement plans for the upcoming year."
    },
    {
        "chunk_id": 13,
        "section": "Exercise Process Steps",
        "content": "Step 1 – Calculate the business results: The Group Finance and Sector/Country CFOs to calculate the full year Financial perspective results, confirm them with the respective Sector/Country Heads before communicating them to the Sector/Country HRBP and the Businesspeople (all bands). The Group HR and Sector/Country HRBPs to calculate the full year People perspective results, confirm them with the respective Sector/Country Heads before communicating them to the Sector/Country HRBP and the Businesspeople (all bands). The Sector/Country CEO to decide on the Customers and Processes perspective results for his respective Sector/BU and communicate them to the Sector/BU HRBP."
    },
    {
        "chunk_id": 14,
        "section": "Exercise Process Leadership and Employee Appraisals",
        "content": "Step 2 – Sector/BU/Country Leadership Team PA: The Sector/Country CEO to conduct the performance appraisal with his Departments' Heads. Step 3 – Employees' PA: The Department Heads and all line managers to conduct the performance appraisal with their team members (1-on-1 physically or on TEAMS for virtual teams and not through email). The Sector/BU CEO to conduct the performance appraisal with his Departments' Heads."
    },
    {
        "chunk_id": 15,
        "section": "Exercise Process Sign-off",
        "content": "Step 4 – sign-off: The Sector/Country HRBP to consolidate and calibrate the performance appraisals' results, ensuring that the overall results of each Band meet the Bell Curve percentage distribution and signs it off from the Sector/Country CEO before submitting the consolidated exercise results to the Group PM (Group.PM@elsewedy.com) before the Sunday 24th November, 2024."
    },
    {
        "chunk_id": 16,
        "section": "Bell Curve Distribution Framework",
        "content": "Bell curve performance appraisal analysis is a graph with a curve shaped like a bell and two tails. It is often used to visualize the distribution of employees across performance as certain values in a graph. The 'Business Goals Achievements' has a immediate reflection on the bell curve shape for the Sector/Country/BU. The Bell Curve is done for each Band(s) separately: 1. One for the Senior Management. 2. One for the Management. 3. One for the Professionals and Senior Professionals combined. 4. One for the Labor. There is a tolerance of (+/-2%) in each point."
    },
    {
        "chunk_id": 17,
        "section": "Bell Curve Distribution Examples",
        "content": "Employees' PA distribution in a Business that Significantly Exceeded Expectations: 0% Unsatisfactory, 10% Needs Improvement, 55% Meets Expectations, 25% Exceeds Expectations, 10% Significantly Exceeds Expectations. Employees' PA distribution in a Business that Exceeded Expectations: 3% Unsatisfactory, 7% Needs Improvement, 60% Meets Expectations, 20% Exceeds Expectations, 10% Significantly Exceeds Expectations. Employees' PA distribution in a Business that Meets Expectations: 5% Unsatisfactory, 15% Needs Improvement, 60% Meets Expectations, 15% Exceeds Expectations, 5% Significantly Exceeds Expectations. Employees' PA distribution in a Business that Needs Improvement: 10% Unsatisfactory, 20% Needs Improvement, 60% Meets Expectations, 7% Exceeds Expectations, 3% Significantly Exceeds Expectations. Employees' PA distribution in a Business with Unsatisfactory Performance: 10% Unsatisfactory, 25% Needs Improvement, 55% Meets Expectations, 10% Exceeds Expectations, 0% Significantly Exceeds Expectations."
    },
    {
        "chunk_id": 18,
        "section": "Performance Appraisal Forms List",
        "content": "Form 1 PA 2024 – Leadership Band, Form 2 PA 2024 - Senior Management Band, Form 3 PA 2024 – Management Band, Form 4 PA 2024 – Professionals Bands – Managing People, Form 5 PA 2024 – Professionals Bands - Individuals, Form 6 PA 2024 – Labor Bands, Form 7 PA 2024 - Consolidation and Analysis."
    },
    {
        "chunk_id": 19,
        "section": "Communication Plan and Deadlines",
        "content": "Action 1: Run 1H training session for the Sector/BU HRBPs and Sector/BU Performance Management Teams on the forms to be used for the performance appraisal exercise. Deadline: 03-11-2024, Owner: Group Performance Management. Action 2: Cascade the guidelines and forms to all businesspeople (all bands) to ensure proper understanding of the guidelines. Deadline: 05-11-2024, Owner: Sector/BU HRBPs. Action 3: Run 1H training bite (Giving and Receiving Feedback) and (Competency Model Refreshment) for all businesspeople (all bands). Deadline: 07-11-2024, Owner: Group Learning and Development."
    },
    {
        "chunk_id": 20,
        "section": "Contact Information",
        "content": "Should you need any further clarifications or questions, please don't hesitate to contact (Group.PM@elsewedy.com). Best regards, Group Chief HR Officer."
    }
],

[{

    "section": "Purpose and Strategic Objectives",
    "content": """
    Purpose: To establish guidelines and procedures for the employee's learning and development within Elsewedy Electric Group and ensure consistency, alignment with organizational goals, employee development, compliance, and optimal resource allocation in training activities. To provide a structured approach for employee learning and development providing clear guidelines accessing training opportunities, participating in development programs, and pursuing career advancement. To ensure the best use of our valuable resources, the policy outlines a process for setting priorities for the Learning & Development budget. Group Learning and Development activities contribute to the achievement of the group's strategic objectives. Accordingly, Elsewedy Electric provides the following training programs to develop and enhance the skills, knowledge, and competencies of our employees: 1. The Learning Hub Programs (HUB) 2. Early Talent Development Programs (ETP) 3. Leadership Development Programs (LDP) 4. Functional Academies Training Programs (FAP) 5. Technical and Vocational Training Programs (TAP)
    """,

    "section": "Applicability and Eligibility",
    "content": """
    Applicability: This policy applies to the Group and all operating companies and subsidiaries directly or indirectly controlled by Elsewedy Electric in all the geographical locations worldwide. Eligibility: This policy applies to all employees of Elsewedy Electric Group, inside or outside of Egypt. It covers all Instructor-led training (ILT), e-learning (EL), classroom or online training, and development activities planned, financed, facilitated, or sponsored by Elsewedy Electric Group. It also aims to align the involvement of all parties in the payment process to guarantee that all sectors/BU have paid their dues to avoid conflicts with external vendors.
    """,

    "section": "L&D Framework and Definitions",
    "content": """
    L&D Framework Definitions: The Learning Hub Programs (HUB): Programs designed to provide competency-based training for all employees of Elsewedy Electric Group. Early Talent Development Programs (ETP): Programs designed to focus on nurturing and developing young talent within Elsewedy Electric Group. Leadership Development Programs (LDP): Programs designed to target high-potential employees, managers, and directors to prepare them for leadership roles within Elsewedy Electric Group. Functional Academies Training Programs (FAP): Programs designed to provide comprehensive learning opportunities focusing on the development of functional competencies. Technical and Vocational Training Programs: Programs designed to develop technical skills and vocational expertise among employees. Instructor-Led Training (ILT): involves traditional classroom or online training sessions facilitated by an instructor. E-Learning (EL): Refers to online training programs that provide employees with the flexibility to learn at their own pace. Internship Program: Undergraduates' Trainings occurs across Elsewedy Electric Group inside or outside Egypt. Graduate Development Program (GDP): A Program designed for recent graduates and aims to develop their skills and knowledge through a structured training plan.
    """,

    "section": "Learning Hub Program Guidelines",
    "content": """
    The Learning Hub Program: All Elsewedy Electric Group employees are entitled to competency-based training programs. The Learning Needs Analysis (LNA) is the primary tool for identifying training needs for business units (BUs), departments, and individual employees based on annual performance appraisals. The L&D team will communicate programs cost and BU enrolment numbers to the Sector/BU HRBPs. HRBPs are responsible for confirming training enrolment and timing with each participant's line manager. In case of excuses from the employee, the HRBP should inform the L&D Team of the participant's absence 10 working days prior to the course/workshop. Each BU covers the cost of booked seats for its employees, regardless of attendance in case of less than 10 working days apology.
    """,

    "section": "Learning Hub Payment Process",
    "content": """
    Training Payments (To confirm the employee's enrolment): 1. For the Sector/BUs that implements Procurement System (Bank Transfers), HRBP shall submit PO document along with the nominations' enrolment sheet prior to the training schedule by minimum 10 working days. 2. For the Sector/BUs that issue payment request, HRBP is responsible for submitting the payment request along with the nominations' enrolment sheet prior to the training schedule by minimum 10 working days. 3. HRBPs are responsible for facilitating payment via cheques or PR System (no cash payment is permitted), within a time frame of 3 weeks from the invoice submission date. 4. HRBPs are responsible for obtaining confirmation from the finance department for the total training cost per BU for the year.
    """,

    "section": "Internship Program Details",
    "content": """
    Internship Program: Under the Internship Program, applicants will be considered based on the criteria below. All Interns must: 1- Be enrolled in their 3rd or final year or recently graduated from universities (including Governmental, Private Universities or International Universities). 2- Pass the selection interview process. The Development Plan tailored to interns across the group is designed as follows: 1- Onboarding. 2- On the Job Training. 3- Competency based trainings. 4- Bonding Activities. 5- Final Project (Group / Individual). 6- Supervision and mentorship (regular feedback & Performance evaluation)
    """,

    "section": "Internship Program Guidelines",
    "content": """
    Internship Program General Guidelines: Internship package amount is determined each year by Group TR team, and to be communicated to BU/Sector HRBP as a fixed amount to all interns. Interns shall commit to the communicated attendance policy. Interns shall achieve 80% of attendance of the Internship Program's duration. Interns shall abide by the organization's dress code. Interns shall respect workplace norms and maintaining confidentiality of sensitive information by signing Non-Disclosure Agreement upon their joining. Interns shall attend all the assigned development activities (On-job-trainings, Training Courses & Induction Program). Interns shall actively engage in open communication with their supervisors, seeking guidance when needed and providing progress updates on assigned tasks. Interns will be assessed by their supervisor based on their performance throughout the program. Interns will be requested to provide feedback on their internship experience highlighting strengths and suggested areas for improvement in the program. In case of low performance and/or violating any of policy's terms and conditions, intern will be excluded from the program immediately and will not be able to receive any monetary allowance and/or certificate of completion, and they will be blacklisted in organization's records.
    """,

    "section": "Graduate Development Program (GDP)",
    "content": """
    Graduate Development Program (GDP): Elsewedy Electric believes that the continuous flow of potential young local talent is an integral part of our talent strategy and is key to sustain and accelerate our growth and designed to sustain and accelerate business growth through 4 main dimensions. Elsewedy Essentials: SWD Way (mission, vision, values, markets, segments..), HSE, security, six sigma, Industrial induction, market visits. Business Essentials: Introduction to function for non-function, Planning, reporting and analysing, IT skills. Knowing and Managing Self: Emotional Intelligence, Critical Thinking, Psychometrics, Abilities, Preferences. Working with Others (Core behaviours & Soft Skills): Effective Communication, Collaboration, Teamwork, Negotiation.
    """,

    "section": "GDP General Guidelines",
    "content": """
    GDP General Guidelines: All GDP employees shall attend Elsewedy Electric General Induction program. Each Sector/BU is responsible to conduct internal orientation program for newly hired GDP employees. The Graduate Development Program offers training courses sponsored by the Group Talent Development budget. Except for the functional trainings requested through the line managers, it will be covered by the Sector/BU's L&D Team. Group Early Talent Team identifies and develops the training programs based on the business needs. GDP employees abroad are granted an E-learning platform access through Group Early Talent Team. GDP Employees are expected to attend 10 mandatory training programs throughout a year. Group Early Talent Team notifies the HRBP of any employee who fails to attend or partially attends training. An employee is defined as a "no show" if he/she fails to notify Group Early Talent Team by the rescheduling request 10 working days prior to the start of the training class. In this case, HRBP is requested to charge the employee/department seat's cost. An employee who misses more than a total of one hour of a training course shall not receive training Certificate. Employees may decide with their line manager to temporarily adjust their work schedule as necessary to allow them to attend the assigned training course. Employees who habitually fail to appear for training are reported to Sector/BU's HRBP as a "commitment issue" which affect his/her overall performance evaluation. GDP Employee shall sign acknowledgment form as part of their hiring process acknowledging that they should attend and complete the assigned development plan (10 Training Courses). Rotation plans will be designed by GDP Employee's line manager and should include specific learning objectives, duration & preferred mentor. Rotation plan that is designed to take place across different business units, GDP Management Team will be responsible for alignment across different BUs' HRBPs to conduct it.
    """,

    "section":" Early Career Development Program (ECDP)",
    "content": """
    Early Career Development Program: The ECDP aims to nurture and advance the careers of employees with 3-5 years of experience, particularly those identified as high potential in senior, team leader, and section head roles. This initiative aligns with Elsewedy Electric's commitment to fostering talent growth and accelerating business development. The ECDP is structured around the following key pillars to facilitate holistic career development for program participants: Skills Enhancement: Providing targeted training and development opportunities focused on core competencies and leadership capabilities. Career Advancement: Offering guidance and resources to help participants map out their career paths within Elsewedy Electric Group. Performance Management: Setting clear performance objectives and providing regular feedback and coaching to support growth and development. The ECDP provides access to training courses sponsored by the Group Learning & Development budget. Training programs are identified and developed by the Group Learning & Development Team based on business needs. Approval from the head of department and HR business partner is required for technical training courses not included in the ECDP Development plan. These courses will be coordinated by the Learning & Development department in each business unit. ECDP participants located abroad will be granted access to an e-learning platform facilitated by the Group Learning & Development Team. Participants are expected to attend 9 mandatory training programs per year. Non-attendance or partial attendance will be reported by the Group Learning & Development Team to the participant's line manager and BU HRBP. Participants must notify the Group Learning & Development Team of any rescheduling requests at least 10 working days before the start of the training class to avoid seat cost charges. Participants must be punctual and attend the entire training session to receive a training certificate. Latecomers (more than 30 minutes after the start) will not be admitted. Missing more than a total of 30 minutes of a training course hour will result in no training credit being awarded. Temporary adjustments to work schedules may be made in consultation with the line manager to facilitate full participation in training.
    """,

    "section":" Leadership Development Programs (LDPs)",
    "content": """
    Leadership Development Programs (LDPs): Targeting the Development of the High Potentials, managers and directors to enroll them in the succession planning for leadership team positions and for key jobs, Elsewedy Electric has designed 2 major learning programs tailored for high potential talents and senior employees. Moreover, retaining them through PDPs where the academies represent a key pillar to accelerating the readiness of the watch-listers. During the Leadership development programs, the attendees will be exposed to business cases, key articles, and group discussions. Program seats allocated among Sector/BU based on the Sector/BU headcount and annual revenue over the last 2 years. Participants have spent at least 2 years in the current Band (Management or Senior Management). Upon passing the Talent Assessment Centre (TAC) the participants are eligible to join any of leadership development programs based on their band. Participant should complete 80% of program's modules, assignments, readings, case studies, live sessions and/or live workshop. Participants receive their certification after successfully fulfilling the program requirements and passing score. Participants who didn't achieve the passing percentage pay the full program fees. In reference to training cost payback, the employee shall fully repay the training program cost if they voluntarily resign within 12 months following the completion of any of the above-mentioned training program.
    """,

    "section":" General Management Development Program (GMDP)",
    "content": """
    General Management Development Program (GMDP): The GMDP program learning criteria is the following: The participants should be in Senior Management Band, among the grades of: D1, D2 & D3. The participants should be nominated from Finance, Sales, Supply Chain & Operations departments. Program seats allocated among Sector/BU based on the Sector/BU headcount and annual revenues. Participants are eligible to join based on nominations by HRBPs across different sectors. Participants will be enrolled in different plans based on developmental TAC results. Participant should complete the program's modules, assignments, readings, case studies, live sessions and/or live workshop. Participants receive their certification after successfully completing the program. Each BU should bear the full amount for the nominated participants. In reference to Training cost payback, the employee shall fully repay the training program cost if they voluntarily resign within 12 months following the completion of any of the above-mentioned training program.
    """,

    "section":" Directors' Development Program (DDP)",
    "content": """
    Directors' Development Program (DDP): The DDP program learning criteria is the following: The participants should be in Senior Management Band, Grades: D1, D2 & D3. The nominations will be for Directors among High Potential / Watch listers on the 9-Box differentiation grid.
    """,

    "section":" Management Development Program (MDP)",
    "content": """
    Management Development Program: The MDP program learning criteria is the following: The participants should be in Management Band, among the grades of: M1, M2 & M3. Program's Recorded Session shall be attended fully in case of missing the Live Training Session.
    """,

    "section":" Functional Academies Overview",
    "content": """
    Functional Academies: Elsewedy Electric Group provides its employees with a comprehensive learning opportunity, focusing on the development of their functional competencies, through developing various Functional Academies, including Sales, Finance, Human Resources, and Supply Chain. These corporate academies are created to ensure that employees learn and master the skills required for the organization to meet its most vital and strategic business needs. Being always up-to date with the best practices and successful concepts in each area of expertise.
    """,

    "section":" Sales Academy",
    "content": """
    Sales Academy: Sales Academy is designed and launched in partnership with one of the top management consultants in the MENA region. The academy is providing learning and development opportunities for all sales team across Elsewedy Electric Group through structured sales track, to enhance sales competencies and skills that is needed to present Elsewedy products and services through optimal methods. HRBP shall be responsible for validating participants lists. HRBP shall align with finance department to ensure the availability of the full program budget for nominated employee's development. HRBP shall be responsible for proceeding with payment once invoice received. Sales Academy participants should be enrolled in a technical assessment before enrolling them into the development path. Nominations will be enrolled based on grades and job levels.
    """,

    "section":" HR Academy",
    "content": """
    HR Academy: HR Academy is designed based on AIHR competency model framework called T-shaped HR Professional. The academy is tackling the HR core competencies in addition to the functional specialist & leadership competency. It offers learning tracks and global certifications across 2 years, that is targeting all job levels to develop HR professionals to be updated with the global HR Trends and support them with the required knowledge and skills to deal within a high growth and complex business environment. Five competencies every HR professional needs: The bar of the T contains the core competencies that are essential for all HR professionals. Each competency is made up of different dimensions. In turn, each dimension is further broken down into specific behaviors, which vary per level of expertise. Specialized Competencies: HR roles have been grouped into six-solution domains. A solution domain is a cluster of functional competencies that deliver value to the business within a particular area of expertise. Nominations will be based on the function/ specialization of the employee. Leadership: HR professionals who have leadership responsibilities will be nominated to leadership development programs based on their seniority level, and their scores in any related assessment to these programs.
    """,

    "section":" Finance Academy",
    "content": """
    Finance Academy: Finance Academy is designed to provide the best development opportunities for finance professionals across 2 years for all group job levels. The academy aims to provide finance professionals with the knowledge and skills that will equip them with the latest trends, information, and technology in the finance industry. The Academy tackles soft, technical and leadership skills. In addition to providing high potential employees with global certifications. Finance Academy Participants are nominated based on the following: Competency Based Track: Participants will be nominated following the general guidelines of Academies nomination practices. Technical Track: 1- Participants will be nominated based on their Function/ Specialization. 2- Participants shall submit any pre & post assessments, placement test and assignments to be able to graduate from the academy. Leadership: Participants will be enrolled in advanced level development track.
    """,

    "section":" Supply Chain Academy",
    "content": """
    Supply Chain Academy: Supply Chain Academy is designed in collaboration with Association of Supply Chain Management (ASCM) the global leader in Supply Chain organizational development and transformation. The Academy is targeting all professional levels across the group. The learning programs are tackling the 6 main pillars of supply chain management. The aim of the academy to let supply chain professionals obtain the global certifications and knowledge which will pave the path for them to excel in their career at Elsewedy Electric. The academies are developed to target all employees' job levels. Participants are divided into three learning tracks (Foundation, Intermediate, Advanced) based on their job level. Foundation learning track is targeting Professionals band, Grades: P1, P2 & P3. Intermediate learning track is targeting Senior professionals and Management Bands, Grades: S1, S2, M1, M2 & M3. Advanced learning track is targeting Senior Management Band, Grades: D1, D2 & D3. Employee's enrolment is based on direct nominations from HRBP in alignment with Line Manager. Each Sector/BU bears the cost of their participants' seats. The participant should give notification 5 working days prior to the training date in case they are not able to attend. The Sector/BU bear the training cost of participant in case of no show without prior notification. Participants receive their certification after successfully completing 80% of training attendance and assignments.
    """,

    "section":" Procurement Track | CIPS",
    "content": """
    Procurement Track | CIPS: Procurement Academy is designed to provide the employees with the opportunity to develop sector-specific knowledge, technical and practical skills, and to apply these skills in work-related environments. This qualification supports learners within operational roles within the procurement and supply professions. CIPS qualifications are regulated internationally to ensure we offer a recognized, professional standard in procurement and supply delivered by EPC Academy. In addition, it is an essential toolkit for anyone planning a career in procurement and supply chain. This academy is based on nominations from the HRBP to ensure that they will be eager to benefit the most from the learning experience. Each business unit should bear the cost of its employees. Each participant should take the placement test to get assigned to the right track based on the score. The scores are the main factor to determine the level as below: Below or equal 40% will be enrolled to Level 2 & Level 3 (advanced) Certificate. From 40% to 65 % will be enrolled to Level 4 Diploma.
    """,

    "section":" Evaluation and Measurement",
    "content": """
    Evaluation and Measurement: Elsewedy Electric measures the training evaluation and effectiveness based on Kirkpatrick model (Reaction, Learning, Behavior and Result). Reaction: Group Learning and development team should send post training evaluation form (Survey Monkey-V2) following the completion of the training with participants to evaluate their satisfaction on the training content, relevance, trainer, engagement, and overall experience. In case the results were less than 70%, analysis should be done to take the required actions for improvement. Learning: Training vendors conduct pre and post assessments for participants on the related topic (if applicable) to evaluate the extent to which the targeted knowledge and skills have been acquired. Behavior: The line manager shall supervise and monitor the participants before and after the course whether applying what they have learned in their jobs and ensure knowledge transfer. Measure the targeted outcome resulted from the training program and report the return on investment of the training.
    """,

    "section":" Internal Trainer Criteria",
    "content": """
    Internal Trainer Criteria: In line with Elsewedy Electric's strategic approach, we aim to leverage the skills and expertise of our internal talents. We emphasize the significance of knowledge transfer within our organization as we strive to achieve our future growth and vision. The L&D team internally announces in case there is a need for an internal trainer based on the training programs required. Interested employees can apply in alignment with Sector/BU HRBP and line managers before being selected as an internal trainer. Interviewing the applicant (Certified / Not Certified), and if he/she is not TOT / TTT certified, the employee to be enrolled to TOT/TTT certification. The employee must spend one year of service within Elsewedy Electric group before being selected as an internal trainer. The employee delivers dry run to a committee from Group Talent Development. The employee is responsible for the training material in alignment with the Group Instructional Design Team. A rewarding system will be applied to compensate Internal Trainers for the spent training hours.
    """,

    "section":" Training Cost Payback",
    "content": """
    Training cost payback: Training cost payback policy aims to ensure that the company has gained the value from the knowledge and learning acquired by the employee post the training program. The training cost is the program fees, in addition to the transportation and accommodation cost (in case of travel abroad). If an employee voluntarily resigns within 12 months following/ within the completion of a training program in which the total training cost exceeds 20,000 EGP (or equivalent in the local market currency) the employee shall repay to the company the training cost on proration based, and if the training cost exceeds 50,000 EGP (or equivalent in the local market currency) the employee shall repay to the company the full training cost. Participant shall sign the training cost pay back agreement form 2 weeks prior the training program. The Sector/BU/participant bear the cost of the training seat in case of no show without prior notification and if the participant failed to accomplish the completion percentage.
    """,

    "section":" Policy Compliance and Discipline",
    "content": """
    Policy Compliance: Elsewedy Electric may conduct regular audits in all its facilities and structures to monitor compliance with this policy. The Group could also conduct internal surveys or initiatives to encourage the employees to always report violations of its policies. All concerns related to the policy shall be freely raised and appropriately handled and followed up by the Group. All Elsewedy Electric staff members are expected to report any case of non-compliance with the policy. The employees should be aware that they have a moral and ethical duty to report such instances and should not fear retaliation. The Group recognizes the importance of confidentiality and could grant anonymity to the complainants who wish so, given that such information does not impede the investigation or resolution of the dispute. There should be no limitation to the filing of complaints, in terms of accessibility to all employees and quantity. The Group will make sure that the employees know where and to whom they can refer for denounces or complaints. Elsewedy Electric ensures that appropriate measures and penalties will be applied in case of non-compliance with this policy. Discipline & Remediation: Violations of this policy may lead to disciplinary action up to, and including, termination of employment/partnership. All disciplinary actions shall be undertaken in accordance with the Group's sanctions list and with all applicable local laws and other legal requirements. The remediation shall be undertaken on a case-by-case basis and in accordance with all applicable local laws and other legal requirements.
    """,

    "section":" Policy Review and Version Control",
    "content": """
    Policy Review: This policy shall be reviewed annually and/or when deemed necessary. Version Control: Title of document: L&D Policy, Version no.: V.01, Document reviewer: Group CHRO, Document approver: Group CHRO, Date of creation: April 2025, Communication & trainings: By BU HRBPs, Date of next review: April 2026, Approved by: Group Chief HR Officer Walid Tayel, Group President & CEO Engineer Ahmed Elsewedy.
    """
}],

[
    {
        "chunk_id": 1,
        "section": "Bonus Pay vs Merit Pay Definitions",
        "content": """What is the difference between the Bonus Pay and the Merit Pay?

The Bonus Pay:
Objective: Is a type of compensation paid to reward the employee's recent (performance) for an elapsed specific period (1-12 months)
Definition: Is considered a (short term) or one-off pay from the company to the employee. If an employee gets a bonus pay for a specific period, this bonus pay will not be carried over forward. Each period is treated separately and therefore the bonus pay varies.
Criteria: The employee's performance = goals achievements (both business and individual) + competencies demonstrated. (refer to the Annual Performance Appraisal Calculation Table in the annex)
Occasion: It is decided based on the Annual End of Year Performance Appraisal exercise results with the Line Manager.

The Merit Pay:
Objective: Is a type of compensation given for the employee's (potentiality) for the future.
Definition: Is considered a (long term) commitment from the company to the employee. If an employee gets a merit pay-based raise, that raise will carry forward its value cumulatively over time. The merit is irreversible.
Criteria: The employee's potential = goals achievements (both business and individual) over the last 2-3 years + capabilities readiness for future role. Capabilities include: the competencies, skills, knowledge, experience … (refer to Talent Capabilities Attributes in the annex)
Occasion: It is decided after the Sector/BU Talent Review Meeting (TRM) between the Sector/BU Head, HRBP and Departments' Heads."""
    },

    {
        "chunk_id": 2,
        "section": "25-Box Grid of Annual Performance Appraisals",
        "content": """(1) The 25-Box Grid of Annual Performance Appraisals' (Bell Curves)

It is a translation of the employee's End of Year Performance Appraisal (EOY PA) ratings for both the Performance Goals' achievements and the Competencies and Behaviors demonstrated. It is developed post the EOY Performance Appraisal to plot the employees on the relevant boxes in preparation for the following exercise (the 9-Box Grid of Talent Differentiation).

Performance Rating Scale:
1: <80% - Unsatisfactory
2: 80%-89% - Needs Improvement
3: 90%-105% - Meets Expectations
4: 106%-120% - Exceeds Expectations
5: >120% (cap to 140%) - Significantly Exceeds Expectations

Actions:
The Sector/BU HRBP to follow the (End of Year Performance Appraisal Exercise Guidelines) previously communicated.

Form:
- Refer to the (End of Year Performance Appraisal Exercise Guidelines) forms.

Deadline: Thursday 28 December 2023"""
    },

    {
        "chunk_id": 3,
        "section": "9-Box Grid of Talent Differentiation",
        "content": """(2) The 9-Box Grid of Talent Differentiation

It is a tool used to measure the (potentiality) of the employees for future jobs either for (succession for key jobs) or (promotion for higher level jobs).

While the 25-Box Grids of Annual Performance Appraisals measure both the Goals' achievements and the Competencies demonstrated, the 9-Box Grid for Talent Differentiation measures the Goals' achievements and the Potential Capabilities of the employee over the last 3 years.

This means that the 9-Box Grid is a consolidation of the last 3 Years of the 25-Box Grid of Annual Performance Appraisals'.

The Employees' Potential Capabilities include the competencies, skills, knowledge, experience … (refer to Talent Capabilities Attributes in the annex)

The 9-Box Grid of Talent Differentiation is developed by the Sector/BU Management Team during the Talent Reviews Meetings (TRM).

The 9-Box Grid of Talent Differentiation is the base for the employees' Merit Increase decisions, and the main input for the for the following exercise of Talent Assessment Centers (TAC)."""
    },

    {
        "chunk_id": 4,
        "section": "9-Box Grid Categories and Distribution",
        "content": """9-Box Grid Employee Categories:

Box 9 - High Potential (HiPo): 5% of employees
- To retain and promote
- Employees who are realizing their full potential while at the same time developing as future leaders at the following levels

Box 6 & 8 - Watch-lister (WL): 15% of employees
- To stretch, develop and retain
- Shows potential for having a greater impact. It's a matter of readiness that prevents them from being a HiPo and moving into those larger roles

Box 3, 5 & 7 - Key Talent, Quality Talent, Solid Performer: 60% of employees
- Consistently meets/usually exceeds. Ready for additional challenge. Potential to perform in another role at same level (transferable skills)

Box 2 & 4 - At Risk, Average Performer: 15% of employees
- At-risk and requires PIP
- Moderate potential for advancement. Strong core competencies within expectations. Engage, focus, motivates to identify potential to higher performance levels

Box 1 - Low Performer (LP): 5% of employees
- Exit 0%
- No potential and below average performance who need to be moved rather quickly to another box or exist plans need to be set"""
    },

    {
        "chunk_id": 5,
        "section": "Talent Review Meeting Actions",
        "content": """Actions for 9-Box Grid Development:

1. Consolidate the 3 years performance appraisal results
The Sector/BU HRBP to consolidate the last 3 years performance appraisal results for each of the 4 Bands separately: Professionals, Senior Professionals, Management and Senior Management.

The Sector/BU HRBP do a draft 3 years 9-Box Grid in preparation for the Talent Reviews Meetings (TRM).

2. Hold Talent Review Meetings (TRM)
The Sector/BU HRBP with the Sector/BU Head and the Management Team to hold a Talent Review Meetings (TRM) day. It is expected to have 60-90 mins discussion for each of the 4 Bands.

The output of this day is the (Final) 9-Box Grid of Talent Differentiation. This exercise is the base for the employees' Merit Increase decisions, and the main input for the following exercise of Talent Assessment Centers (TAC).

Form:
- The 9-Box Grid of Talent Differentiation Guidelines
- Talent Review Meeting Worksheet

Deadline: Monday 08 January 2024"""
    },

    {
        "chunk_id": 6,
        "section": "Merit Increase Principles",
        "content": """(3) The Merit Increase

There is NO fixed Merit Increase % that is applied to all employees. Merit increase % is decided within the following 5 principles:

1. The Type of Sector (industry) and its Pay Scale.
No action required (included in the Gap Analysis document done by the Group Total Rewards)
We operate in different Sectors: Manufacturing, Energy, Engineering and Construction, Digital and Corporate. Each Sector has its own pay scale in the market. Within the same Sector, businesses are at a different stage of growth and maturity.

2. The Market Movement for this specific Sector in a specific country.
No action required (included in the Gap Analysis document done by the Group Total Rewards)
The Group Total Rewards to study the market movement for each Sector, analyzes the pay gap versus the market (by Band), and communicates it to the Sector/BU Head, HRBP and Finance Head.

3. The targeted Pay Segment.
No action required (included in the Gap Analysis document done by the Group Total Rewards)
While communicating the pay gap analysis, the Group Total Rewards considers the targeted pay segments. The pay segment is the targeted positioning of the company versus its peer group in the market. During this step, the Group Total Rewards considers the different types of jobs in the Company:
• For the Core-Jobs and Leadership Band jobs, the chosen Pay Segment is the 75th Percentile
• For the Support Functions jobs (enabling), the chosen Pay Segment is the 65th Percentile
• For the Workers and Technicians jobs, the chosen Pay Segment is the 50th Percentile"""
    },

    {
        "chunk_id": 7,
        "section": "Merit Increase - Employee Potentiality and Pay Points",
        "content": """4. The Potentiality and Current Pay of the Employee.

Actions:
The Sector/BU HRBP to use the (Gap Analysis document) received from the Group Total Rewards to decide on the Merit Increase for each Employee considering 2 variables:
1. The Employee's targeted Pay Point based on his/her Potentiality. Employee's Potentiality represents his/her position on the 9-Box Grid of Talent Differentiation.
2. The Employee's current Pay Point.

The Targeted Pay Point based on Potentiality is as follows:
• High Potential Employees (in box no.9) basic salary should be positioned at a pay point above between 110%-130% from their relevant Pay Segment.
• Watch-Lister Employees (in box no.6 and 8) basic salary should be positioned at a pay point between 90%-110% from their relevant Pay Segment.
• Key Talent, Quality Talent, and Solid Performers' employees (in box no.3, 5 and 7) basic salary should be positioned at a pay point between 80%-100% from their relevant Pay Segment.
• At Risk Employees (in box no.2 and 4) basic salary should be positioned at a pay point between 60%-80% from their relevant Pay Segment.
• Low Performers Employees (in box no.1) should get the minimum salary increase possible as per the country's law and their pay should not be more than 70% from their relevant Pay Segment.
• It is highly recommended that each Sector/BU build a provision for the exit packages of the confirmed low performers in case they don't improve after the 3-months Performance Improvement Plan (PIP).

Form:
- Merit Increase Form 2024
- Talent Review Meeting Worksheet

Deadline: Thursday 11 January 2024"""
    },

    {
        "chunk_id": 8,
        "section": "Financing Ideas for High Performers",
        "content": """Ideas to finance the extra pay for the HiPo and Watch-Listers

• Set exit plans for Low Performers employees (in box no.1) and use their pay in offering extra compensation for the HiPo.
• Revise the Manpower Plan for the next year, merge jobs instead of hiring and offer extra compensation for the HiPo.
• Revise the other SG&A expenses (e.g. utilities, rentals, travel …), reduce the cost and use this amount in offering extra compensation for the HiPo.

Pay Range Distribution:
HiPo Talent: 5% of the employees from each Band (110%-130% pay range)
Watch-Listers: 15% of the employees from each Band (90%-110% pay range)
Key Talent: 60% of the employees from each Band (80%-100% pay range)
At Risk employees: 15% of the employees from each Band (60%-80% pay range)
Low Performers employees: 5% of the employees from each Band (50%-70% pay range)"""
    },

    {
        "chunk_id": 9,
        "section": "Budget Considerations and Approval Process",
        "content": """5. The available Budget for the Merit Increase.

Action:
The Sector/BU HRBP and the Finance Head to do a financial simulation for the Merit Increase. The key ratio to consider is (the Personnel Cost / the Budgeted Sales) versus the previous year's ratio. The % of (Personnel / Sales) 2024 should be < or = % of (Personnel / Sales) 2023.

Personnel cost includes all the wages and salaries in addition to other personnel expenses. Personnel cost 2024 = personnel cost 2023 + merit increase 2024 + manpower plan 2024. (refer to the Personnel Expenses Table in the annex)

The Promotions' cycles are planned in April and October. A special budget to be provisioned to finance the Promotions in both cycles. (refer to the Promotions Guidelines document)

The Sector/BU HRBP to sign-off from the Sector/BU Head the
1. The initial Merit Increase, and
2. Talent Review Meeting Worksheet

And submits them to the Group Total Rewards (Group.Reward@elsewedy.com) for revision.

Deadline: Sunday 14 January 2024

The Group Total Rewards to sign-off the Merit Increase from the Group CHRO, Group CFO, Group CEO and finally from the Group Compensation Committee and confirms back to the Sector/BU HRBP for implementation.

The revision will be based on the above mentioned 5 principles.

Deadline: Thursday 18 January 2024

Once approved, the Sector/BU HRBP to implement the Merit Increase figures on the system. It is recommended that the Sector/BU HRBP communicates the Merit Increase through personalized digital letters to the employees especially the HiPo Talent."""
    },

    {
        "chunk_id": 10,
        "section": "Step-by-Step Process for HRBP",
        "content": """Step-by-step for the Sector/BU HRBP

After the Talent Review Meeting (TRM) and competing the (9-Box Grid for Talent Differentiation),

1. Get the needful data for each Band.
2. Check the Employee's (Potentiality Position) on the 9-Box Grid.
3. Work on the Merit Pay by employee to reach the Targeted Coma-Ratio relevant to his/her Potentiality Position. Start the increase from right to left, from the HiPo Employees as they represent the priority in the merit exercise.
4. Do the same for the 4 Bands.
5. You will end up with the following table.

Band Structure:
- Senior Management
- Management
- Senior Professionals
- Professionals
- Technicians & Workers

Categories: Low Performers | At Risk | Key Talent | Watch-listers | HiPo

6. (Merit Increase Grand Total Value + Manpower Plan 2024) / Sales Budget 2024 = Personnel Cost 2024
7. (Personnel Cost 2024 / Sales Budget 2024) % should be = or < (Personnel Cost 2023 / Sales Budget 2023) %
8. If the 2024 ratio is > than 2023 ratio, you need to re-do the step number 3 above. Start the deduction from left to right, from the Low Performers and At-Risk Employees till you reach the targeted personnel cost / sales budget ratio.
9. Once the Group Total Rewards compete the revision (as per the below table) and sign-off process, you can proceed with the Merit Pay implementation."""
    },

    {
        "chunk_id": 11,
        "section": "Performance Appraisal Calculation Table",
        "content": """The Annual Performance Appraisal Calculation Table

Performance Appraisal Calculation by Band:

Band 1 - Leadership:
- Individual Goals' Achievement: 20%
- Business Goals' Achievement: 60%
- Core & Leadership Competencies: 20%

Band 2 - Senior Management:
- Individual Goals' Achievement: 40%
- Business Goals' Achievement: 40%
- Core & Leadership Competencies: 20%

Band 3 - Management:
- Individual Goals' Achievement: 60%
- Business Goals' Achievement: 20%
- Core & Leadership Competencies: 20%

Band 4 - Senior Professional:
- Individual Goals' Achievement: 80%
- Business Goals' Achievement: 20%
- Core Competencies: 20%

Band 5 - Professional:
- Individual Goals' Achievement: 80%
- Core Competencies: 20%"""
    },

    {
        "chunk_id": 12,
        "section": "Personnel Expenses Breakdown",
        "content": """The Personnel Expenses Breakdown

Personnel Cost (direct & indirect)

Considered in the Manpower Plan Sheet:
- Basic Salaries
- Allowances
- Bonus
- Insurance

NOT considered in the Manpower Plan Sheet (*you need to consider in your total personnel cost calculation):
- Incentives
- Overtime
- Retirement
- Meals
- Uniform
- Awards
- Medical
- Training Expenses
- Travel Expenses
- Transportation Expenses
- Other Benefits
- Other Personnel

Wages & Salaries category includes both considered and not considered items for comprehensive personnel cost calculation."""
    }
],

[
    {
        "chunk_id": 1,
        "section": "Purpose and Applicability",
        "content": "This policy is designed to guide employees on the required standards of dress and appearance. Employees must maintain an appropriate standard of dress and personal appearance at work and conduct themselves in a professional manner at all times both within the workplace and when representing the Company. This Policy is a minimum standard; where local legislations define higher standards; the Group shall comply with them. This policy applies to all the operating companies and subsidiaries directly or indirectly controlled by Elsewedy Electric, and all the geographical regions where Elsewedy Electric companies and subsidiaries are operating."
    },
    {
        "chunk_id": 2,
        "section": "Definitions",
        "content": "Business Formal Dress Code includes suits and ties for men, while women require business suits with pants or a long skirt and a jacket. Semi-Formal Dress Code includes suits, jackets, shirts, skirts and pants that are typical of formal business attire at work."
    },
    {
        "chunk_id": 3,
        "section": "Roles and Responsibilities",
        "content": "The following personnel have roles and responsibilities with regard to the implementation of this policy as described in detail in the Principles and Procedures section: BUs HRBP to assure the application of this policy. HR Operations team to apply the internal disciplinary actions for policy violation."
    },
    {
        "chunk_id": 4,
        "section": "Office Dress Code Rules",
        "content": "As representatives of Elsewedy Electric Group, employees should adhere and abide by the following dress code guidelines: Formal or Semi-Formal: suits, jackets, shirts, skirts, and pants that are typical of formal business attire at work. The company requires employees to always dress neatly, appropriately, and that they maintain adequate personal hygiene. All clothing shouldn't have tears, rips or holes, even if it is the current fashion. Clothes should be professional, which means that it should not be too revealing, or having any stamps or prints that are offensive or inappropriate. On Thursdays, smart casual wear is accepted. Jeans, Polo Shirts, T-shirts (no drawings), sneakers are accepted. Slippers, shorts, ripped jeans and sportswear are not allowed even during Thursdays. On Thursdays, The direct manager has the right to decide the appropriate attire of his team according to the job nature. Females are allowed to wear jewelry. However, any visible body piercings during working hours are not allowed. Employees on a mission outside the office can wear either formal or casual depends on the nature of the mission and after obtaining approval the direct manager."
    },
    {
        "chunk_id": 5,
        "section": "Office Personal Hygiene Requirements",
        "content": "At all times employees should comply with the following: Neat haircut. Trimmed beard, mustache, and whiskers. Personal hygiene. Proper and clean nails."
    },
    {
        "chunk_id": 6,
        "section": "Site and Factory Dress Code",
        "content": "The employees must comply to wearing the appropriate attire for the sites and ensure the health and safety regulations as following: Safety helmet with Elsewedy electric logo. Safety glasses and any other required safety equipment for their work area. Clean and ironed coverall. Personal protective equipment should be worn according to HSE department instructions."
    },
    {
        "chunk_id": 7,
        "section": "Uniformed Personnel Requirements",
        "content": "The uniform should always be clean, neat, in a good shape, and pressed and the employees must maintain adequate personal hygiene. All employees must change before leaving the premises and It is not allowed to wear your uniform off duty. Each employee must take personal care of his/her uniform. Any intentional damage caused to the uniform will have to be compensated by the employee."
    },
    {
        "chunk_id": 8,
        "section": "Dress Code Violations and Enforcement",
        "content": "The company has the right to warn an employee who does not comply with the dress code guidelines according to the internal disciplinary actions policy and as per the labour law of each country. Managers or supervisors are expected to inform employees when they are violating the dress code. This may include having to leave the work to change clothes. Repeated violations or violations that have major repercussions may lead the HR operations team to apply disciplinary action being taken up to and including termination."
    },
    {
        "chunk_id": 9,
        "section": "Policy Compliance and Reporting",
        "content": "Elsewedy Electric may conduct regular audits in all its facilities and structures to monitor compliance with this policy. The Group could also perform internal surveys or initiatives to encourage the employees to always report violations of its policies. All concerns related to the policy shall be freely raised and appropriately handled and followed up by the Group. All Elsewedy Electric staff members are expected to report any case of non-compliance with the policy. The employees should be aware that they have a moral and ethical duty to report such instances and should not fear retaliation. The Group recognizes the importance of confidentiality and could grant anonymity to the complainants who wish so, given that such information does not impede the investigation or resolution of the dispute. There should be no limitation to the filing of complaints, in terms of accessibility to all employees and quantity. The Group will make sure that the employees know where and to whom they can refer for denounces or complaints. Elsewedy Electric ensures that appropriate measures and penalties will be applied in case of non-compliance with this policy."
    },
    {
        "chunk_id": 10,
        "section": "Discipline and Remediation",
        "content": "Violations of this policy may lead to disciplinary action up to, and including, termination of employment/ partnership. All disciplinary actions shall be undertaken in accordance with the Group's sanctions list and with all applicable local laws and other legal requirements. The remediation shall be undertaken on a case-by-case basis and in accordance with all applicable local laws and other legal requirements."
    },
    {
        "chunk_id": 11,
        "section": "Policy Review Schedule",
        "content": "This policy shall be reviewed annually and/or when deemed necessary."
    }
],

[
    {
        "section": "Purpose",
        "content": "To maintain standards for the car allowance at Elsewedy Electric Factories. It is provided for the top management, it is considered an attraction and retention tool, reflecting the BU's success, and enhancing its brand image."
    },

    {
        "section": "Applicability",
        "content": "This policy applies to all factories controlled by Elsewedy Electric. Geographical Locations: Egypt – Industrial Zones"
    },

    {
        "section": "Definitions",
        "content": "Eligible Employees: Employees who are allowed to receive a BU car allowance based on the Table of Benefits. Acknowledgment or payback Doc: A written legal document that outlines the terms of a pay agreement."
    },

    {
        "section": "Roles & Responsibilities",
        "content": "The following personnel have roles and responsibilities regarding the implementation of this policy as described in detail in the Principles and Procedures section. The Group Total Reward & The Group Organization Design: Design and Update the policy. BUs HRBP: Implementing and approving the car allowance based on the policy. Finance Director/CFO: Budget approval. GM/MD/CEO: Final approval"
    },

    {
        "section": "Eligibility Criteria",
        "content": "The car allowance is eligible for the factory's top management and they are: The Factories Managing Directors / General Managers. The BU Management, employees on the Senior Management and Management bands."
    },

    {
        "section": "Policy Principles - General",
        "content": "Eligibility: car allowance is provided based on job level, as per the Table of Benefits. The HRBP should abide by the criteria mentioned in the Table of Benefits attached. The Car Allowance will be paid fully to the eligible employee via Bank check or cash to be handed to the employee based on the Table of Benefits."
    },

    {
        "section": "Policy Principles - Implementation Conditions",
        "content": "It is not mandatory for the company to pay this amount on the date of joining, but the company has the freedom to do a gradual and selective implementation. The employee signs an Acknowledgment or a payback form that contains an agreement, mentioning that the employee needs to stay for the following 5 years from receiving the allowance And/OR a trust receipt with the full amount. In the case of the trust receipt, It is to be handed to the employee after the completion of the 5 years. In case the employee leaves the company, he/she needs to pay back the remaining amount of the received allowance pro-rata. The allowance is to be renewed not before 5 years and based on the BU Head approval and the BU financial capabilities."
    },

    {
        "section": "Policy Principles - Retirement Provisions",
        "content": "In Case the Eligible employee is approaching retirement age during the 5 years, he will be eligible for a prorated amount till the date of retirement."
    },

    {
        "section": "Policy Process & Procedure - Steps",
        "content": "Each BU has the freedom to develop its procedures based on this policy to provide eligible employees gradually with a car allowance through the following process: 1. The BU HRBP in each factory is responsible for defining the employees and preparing a list with their names. 2. The BU HRBP submits the list to the Group Organization Design Department to confirm their grades and job level. 3. The Group Organization Design team reviews and confirms the employee's levels during 3 working days. 4. The BU HRBP submits the budget to the Finance department for approval after granting the BU Head approval on the employees list. 5. The BU HRBP pays the car allowance based on the confirmed list from the Group Organization Design department."
    },

    {
        "section": "Payback Calculation Example",
        "content": "Example: An employee who spent 3 years and eligible for 1,000,000, decided to leave the company before completing the obligatory 5 years, the calculation will be as follows: Car Allowance per month = 1,000,000 (Total allowance) / 60 months obligatory duration = 16,667 per month. Payback Duration = Total obligatory duration in months (60 months) - Spent duration in months (36 months) = 24 months. The payback amount = Payback Duration (24 months) * Car Allowance per month (16,666 per month) = 400,000 EGP"
    },

    {
        "section": "Retirement Calculation Example",
        "content": "Example: Employee who is 58 years old, and is eligible for 1,000,000 car allowance the calculation will be as follows: Car Allowance per month = 1,000,000 (Total allowance) / 60 months obligatory duration = 16,667 per month. Car allowance eligible amount = 24 months to retire * 16,667 per month = 400,000"
    },

    {
        "section": "Rectification of the Situation",
        "content": "The company will no longer assign cars to employees, instead the car allowance will be implemented. Employees who previously had an assigned company car will be substituted with the car allowance as per this policy and the car to be returned to BU. The returned cars will be under the custody of the BU, fully utilized as needed for business purposes. The current depreciated cars zero book value to be put up for closed envelope auction for all employees. Approval from the financial department is required before proceeding with the auction. The cars to be managed by the Administration/Transportation department. The rectification should take place before the end of Q1 2025."
    },

    {
        "section": "Policy Compliance",
        "content": "Elsewedy Electric may conduct regular audits in all its facilities and structures to monitor compliance with this policy. The Group could also perform internal surveys or initiatives to encourage the employees to always report violations of its policies. All concerns related to the policy shall be freely raised and appropriately handled and followed up by the Group. All Elsewedy Electric staff members are expected to report any case of non-compliance with the policy. The employees should be aware that they have a moral and ethical duty to report such instances and should not fear retaliation. The Group recognizes the importance of confidentiality and could grant anonymity to the complainants who wish so, given that such information does not impede the investigation or resolution of the dispute. There should be no limitation to the filing of complaints, in terms of accessibility to all employees and quantity. The Group will make sure that the employees know where and to whom they can refer for denounces or complaints. Elsewedy Electric ensures that appropriate measures and penalties will be applied in case of non-compliance with this policy."
    },

    {
        "section": "Discipline & Remediation",
        "content": "Violations of this policy may lead to disciplinary action up to, and including, termination of employment/ partnership. All disciplinary actions shall be undertaken in accordance with the Group's sanctions list and with all applicable local laws and other legal requirements. The remediation shall be undertaken on a case-by-case basis and in accordance with all applicable local laws and other legal requirements."
    },

    {
        "section": "Policy Review",
        "content": "This policy shall be reviewed annually and/or when deemed necessary."
    },

    {
        "section": "Table of Benefits",
        "content": "Car Allowance TOB - Egypt Industrial Zones. Leadership - Managing Director: 1,000,000 EGP. Senior Management - Factory / General Manager: 1,000,000 EGP, Directors: 750,000 EGP. Management - Senior Manager: 500,000 EGP, Managers: 500,000 EGP."
    },

    {
        "section": "Policy Related Documents",
        "content": "Document Name: Acknowledgment"
    },

    {
        "section": "Version Control",
        "content": "Title of document: Car Allowance - Egypt Industrial Zones. Version no.: V.01. Document owner: Group Total Reward. Date of creation: Dec. 2024. Date of next review: Dec. 2025. Group Chief HR Officer: Walid Tayel. Group President & CEO: Engineer Ahmed Elsewedy"
    }
],

[
    # Chunk 1: Document Overview and Purpose
    {
        "id": "overview",
        "section": "Manpower Planning 2025 Overview",
        "content": """Exercise 02. Manpower Planning 2025
As we are in the process of developing the 2025 annual budget, we are glad to kick-off the (Manpower Planning) exercise.
Please read the below carefully before staring the exercise."""
    },

    # Chunk 2: Position Definitions - GDP
    {
        "id": "gdp_definitions",
        "section": "Graduate Development Program Positions (GDP)",
        "content": """Graduate Development Program positions (GDP)
- Grade P3.
- Criteria: from 0 up to 2 years of experience.
- Job titles: GDP Specialist, Junior Engineer, or Coordinator."""
    },

    # Chunk 3: Position Definitions - ET
    {
        "id": "et_definitions",
        "section": "Early Talent Positions (ET)",
        "content": """Early Talent positions (ET)
- Grade P2 and P1.
- Criteria: more than 2 years of experience and below 29 years old.
- Job titles: engineer, specialist, senior engineer and senior specialist."""
    },

    # Chunk 4: Position Definitions - MCR
    {
        "id": "mcr_definitions",
        "section": "Mid-Career Recruit Positions (MCR)",
        "content": """Mid-Career Recruit positions (MCR)
- Grade S2, S1, M3, M2, M1.
- Job titles: team leader, section head, manager, and senior manager"""
    },

    # Chunk 5: Position Definitions - SP
    {
        "id": "sp_definitions",
        "section": "Senior Positions (SP)",
        "content": """Senior Positions (SP)
- Grade D3, D2, D1 and L3, L2, L1.
- Job titles: director, general manager, managing director and C level."""
    },

    # Chunk 6: Personnel Cost Formula
    {
        "id": "personnel_cost_formula",
        "section": "Personnel Cost 2025 Calculation",
        "content": """Personnel Cost 2025 =
- Personnel Cost 2024
- + Merit Increase 2025 (on the basic salary for the 2024 Headcount)
- + Manpower Plan 2025 Personnel Cost (new hires & replacements)
- + Salary Adjustments 2025 (planned in Apr and Oct every year)

Personnel Cost 2025 / Sales Budget 2025 (%) should be = or < Personnel Cost 2024 / Sales Budget 2024 (%).

If not, any of the Merit, or Manpower, or Sales budgets should be revised. This means that the rule of '10% extra manpower plan' is NO more valid. The Manpower Plan is a cost that should be correlated to the Sales Growth, Efficiency and other Productivity KPIs."""
    },

    # Chunk 7: Merit Increase Information
    {
        "id": "merit_increase_info",
        "section": "Merit Increase 2025 Details",
        "content": """The estimated budget for the Merit Increase 2025 in Egypt is set at 20% on the Basic Salary, till the issuing of the Salary Surveys by our partners in December.

The Salary Surveys are issued by industry or business sector, and by country.

For the companies outside Egypt, please contact the Group Total Rewards (Group.Reward@elsewedy.com) to know the expected market movement in your country.

The Merit Increase % and budget is subject to approval by the Compensation Committee (Board Committee) in January 2025."""
    },

    # Chunk 8: Personnel Cost Components
    {
        "id": "personnel_cost_components",
        "section": "Personnel Cost Components",
        "content": """Personnel Cost (direct & indirect)

Considered in the Manpower Plan Sheet:
- Basic Salaries, Incentives
- Allowances, Overtime
- Bonus, Retirement
- Insurance, Meals
- Uniform, Awards

NOT considered in the Manpower Plan Sheet (*you need to consider in your total personnel cost calculation):
- Medical, Training Expenses
- Travel Expenses
- Transportation Expenses
- Other Benefits"""
    },

    # Chunk 9: Manpower Plan Split Requirements
    {
        "id": "manpower_split_requirements",
        "section": "Manpower Plan Headcount Split",
        "content": """The Manpower Plan Headcount to be split as follows:
- 75% or more of the new hires and replacement for GDP and ET
- 25% and NOT more of the new hires and replacement for MCR & SP

It does not matter for the time being if your BU strictly follows the 2024 structure or not. The sheet will give us an estimate figure for the 2025 estimated Personnel Cost with (+/-) 10% accuracy."""
    },

    # Chunk 10: Exercise Process - BU Level
    {
        "id": "exercise_process_bu",
        "section": "Exercise Process - Business Unit Level",
        "content": """The BU HRBP to complete the manpower plan with the Heads of Departments and sign it off from the BU Head before submitting it to the Sector/Country HRBP."""
    },

    # Chunk 11: Exercise Process - Sector Level
    {
        "id": "exercise_process_sector",
        "section": "Exercise Process - Sector/Country Level",
        "content": """The Sector/Country HRBP to consolidate the BUs manpower plans into 1 plan, revise it, review/confirm it with the Group OD based on the confirmed graded structure, then sign it off from the Sector/Country CFO and Sector/Country Head before submitting it to the Group TA Team (Group.TA@elsewedy.com)."""
    },

    # Chunk 12: Exercise Process - Group Support
    {
        "id": "exercise_process_group_support",
        "section": "Exercise Process - Group Support Departments",
        "content": """For the Group Support Departments (Finance, Human Resources, Information Technology, Legal, Compliance, Audit and MarCom), the Sector/Country HRBP to discuss the manpower plans with the Group Support Department HRBP and Group Support Department Head.

The Group Support Department HRBP review/confirm the support departments manpower plans with the Group OD based on the confirmed graded structure before submitting it to the Group TA Team (Group.TA@elsewedy.com).

The Group Support Departments to comply with the Group vs Sector SOD (Segregation of Duties) guidelines (which positions are at Group level only, which positions are at Sector level only and which positions are at both levels).

As well as to the Department's EPI (Employee Productivity Index)."""
    },

    # Chunk 13: Exercise Process - Final Approval
    {
        "id": "exercise_process_final",
        "section": "Exercise Process - Final Approval",
        "content": """The Group TA Team to consolidate and revise the manpower plan sheets and sign them off from the Group CHRO followed by the Group CFO and Group CEO."""
    },

    # Chunk 14: Hiring Guidelines - Start Date
    {
        "id": "hiring_guidelines_start_date",
        "section": "Hiring Start Date Guidelines",
        "content": """Set the hiring start date -as much as possible- to be 01 March, this will allow the Business HRBP after the Performance Appraisal Exercise and Talent Review Meetings 'TRM' to leverage on our internal pool of talent to fill the manpower requirements before looking outside."""
    },

    # Chunk 15: Hiring Guidelines - Quarterly Distribution
    {
        "id": "hiring_guidelines_quarterly",
        "section": "Quarterly Manpower Distribution",
        "content": """Spread the manpower plan across the year to be as follows: 10% for Q1, then 30% equally for Q2, Q3 and Q4 excluding project based and labor requisitions that can be fulfilled anytime as per business needs."""
    },

    # Chunk 16: Hiring Guidelines - Prioritization
    {
        "id": "hiring_guidelines_prioritization",
        "section": "Hiring Prioritization Guidelines",
        "content": """Prioritize the new manpower that will generate extra sales and profit and reduce or postpone the rest of the manpower. So please keep the hiring of support departments at its minimum level to improve the ratios of support functions vs front office."""
    },

    # Chunk 17: Internal Talent Pool Guidelines
    {
        "id": "internal_talent_guidelines",
        "section": "Internal Talent Pool Usage",
        "content": """Use the internal pool of HiPo Talent (high potentials) to fill the manpower requirements before looking outside. Refer to the Group Talent Management Team to advise you with internal potential talent across the Group (Group.TM@elsewedy.com), especially projects'-based BUs like the EPC and Infrastructure Sectors."""
    },

    # Chunk 18: Open Job Posting Process
    {
        "id": "open_job_posting_process",
        "section": "Group Open Job Posting Process",
        "content": """Contact the Group Talent Acquisition Team to use the Group Open Job Posting 'OJP' (Group.IM@elsewedy.com), to post the vacancies internally before proceeding with the external hires.

The OJ (Open Job) HRBP to share the position open for internal posting either by marking it on TALEO or by sending it to the Group Internal Mobility Team (Group.IM@elsewedy.com)

The interested Employee (Applicant) to discuss the opportunity and share his/her interest with his/her Line Manager and HRBP. (the applicant should have spent at least 1 year in the current job and the minimum rating in the last PA is 3 'meeting expectations').

The Applicant's Line Manager and HRBP to approve or reject the application.

If accepted, the (Applicant) to apply on TALEO or send his/her CV to the Group Internal Mobility Team (Group.IM@elsewedy.com) copying his/her Line Manager and his/her HRBP.

The Group Internal Mobility Team to screen the CVs and share the shortlist of Applicants with the (OJ Line Manager) and the (OJ HRBP).

The interviews take place, the best candidate is accepted.

The Group Internal Mobility Team to align with the (Applicant's Line Manager) and (HRBP).

The transfer happens between the (Applicant's HRBP) and (OJ HRBP)."""
    },

    # Chunk 19: Expatriation Guidelines
    {
        "id": "expatriation_guidelines",
        "section": "Expatriation Guidelines",
        "content": """For all the roles open for Expatriation at all levels:

Make sure you assign them to the HiPo employees in your business or other BUs in Elsewedy Electric Group and do not proceed with a new hire unless the required capabilities are not available in the Group.

The Group Talent Acquisition Team to champion this with the Group Talent Management Team to make sure we open all the learning opportunities to our HiPo, fulfill their career ambitions and make the best use out of their potential.

As announced before, all expatriation offers to be issued by the Group Total Rewards (Group.Reward@elsewedy.com) and signed by the Group CHRO and Group CEO."""
    },

    # Chunk 20: Plan Revision Schedule
    {
        "id": "plan_revision_schedule",
        "section": "Manpower Plan Revision Schedule",
        "content": """Once submitted and approved, this annual manpower plan is considered final for Q1 plan. The Group TA recruiter's deployment and the Group Employer Branding attraction plan will be set accordingly. Q2 to Q4 plans are subject to the quarterly revision 45 days prior to the quarter beginning (15 Feb for Q2, 15 May for Q3 and 15 Aug for Q4)."""
    },

    # Chunk 21: TALEO System Requirements
    {
        "id": "taleo_system_requirements",
        "section": "TALEO System Requirements",
        "content": """Once the manpower plan is approved, all the hiring requisitions to be done through TALEO prior to starting the search for the candidates.

The Group TA team will NOT proceed with requisitions coming through (phone calls, emails, meetings …).

All job offers to be issued through TALEO."""
    },

    # Chunk 22: Contact Information
    {
        "id": "contact_information",
        "section": "Contact Information",
        "content": """Should you need any further clarifications or questions, please don't hesitate to contact (Group.TA@elsewedy.com)

Best regards,
Walid Tayel
Group Chief HR Officer"""
    },

    # Chunk 23: Employee Productivity Index Table
    {
        "id": "epi_table",
        "section": "Employee Productivity Index (EPI) 2024-2025",
        "content": """Employee Productivity Index (EPI) 2024-2025
Department | Market Benchmark
Finance | 80 Finances: 1 billion $ revenues
         | a. Less than 50 Employees = 1 HR: 100 Employees
         | b. From 50 to 100 Employees = 2.5 HR: 100 Employees
         | c. From 100 to 500 Employees = 1.5 HR: 100 Employees
         | d. From 500 to 1,000+ = 1.3: 100 Employees
HR       | a. Less than 2,500 Employees = 1 IT Support:70-100 Employees
         | b. From 2,500 to 7,500 Employees = 1 IT Support: 130-175 Employees
         | c. More than 7,500 Employees = 1 IT Support: 200-300 Employees
IT Support| 14 FTE: 1B$
Legal    | """
    }
],

[
    {
        "section": "purpose_and_scope",
        "content": """Purpose: The Global Mobility policy serves as a strategic roadmap for ELSEWEDY ELECTRIC group that benefits business and employees alike. For the business, it develops and retains a globally competent workforce, enhances market penetration, mitigates risks associated with global operations, fosters a culture of innovation and cross-cultural collaboration, all while optimizing costs. For the employees, it offers opportunities for professional growth, career development, and accelerate the talent readiness while managing international assignments.

Applicability: This policy applies to the Group and all operating companies and subsidiaries directly or indirectly controlled by Elsewedy Electric in all the geographical locations worldwide."""
    },

    {
        "section": "eligibility_criteria",
        "content": """Eligibility: Any role which involves working and travelling across country borders significantly adds to the complexity and costs of running the business. Therefore, there is a responsibility on all managers to ensure that the employees requested to undertake cross border activities meets the below requirements:
- "Hipo or Watch-lister" - an employee who is identified as having the potential to move further through the organization (located in boxes 6,8, and 9 in the 9-Box Grid of Talent Differentiation).
- "Expert" - an employee who is recognized across the business as an expert in their field and capable of transferring knowledge."""
    },

    {
        "section": "mobility_types_definitions",
        "content": """Global Mobility Types by Duration:
1. Business Trip: 1 – 30 Calendar Days
2. Short Term Assignment 'STA': > 30 Calendar Days – 12 months
3. Long Term Assignment 'LTA': 1 Year – 2 Years
4. Local Terms: Full Transfer
5. Project Based Assignment: As per the project plan

Key Definitions:
- Home Country: The country where the employee worked prior to the international assignment.
- Host Country: The country where the employee works during the international assignment.
- Short Term Assignment (STA): This is a temporary transfer, when a duration is less than 12 months, the employee signs a letter of assignment, and his current job is secured with the same grade by the home country BU.
- Long Term Assignment (LTA): This is a temporary long-term assignment, when a duration is more than 12 months, and a maximum of 2 years, the employee signs a letter of assignment, and his current job or higher is secured by the home country BU.
- Letter of Assignment: The offer issued by Group Total Rewards and the Sector HRBP and signed by the employee for the STA or LTA. It includes the start and end date and the benefits provided to the employee during the assignment.
- Localization Terms: This is a permanent transfer; the employee is treated as a local employee in terms of compensation and benefits."""
    },

    {
        "section": "compensation_allowances_definitions",
        "content": """Compensation and Allowances Definitions:
- Pay Matrix: the table that includes the pay and benefits elements for each country separately, it will be developed and annually updated by Group Total Rewards.
- COLA (Cost of Living Allowance): This allowance is designed to cover additional living expenses during assignment, such as laundry, goods, and services, ensuring the employee can maintain a suitable standard of living. it will be developed and annually updated by Group Total Rewards according to the hosting country local and economic conditions.
- Hardship Allowance: provided to employees who are assigned to countries with challenging living conditions. The level of the Hardship Allowance is determined by the nature of the country and the difficulty of the living conditions, identified and annually updated by Group Total Rewards using the annual market survey reports.
- Furnished apartment: means that basic furniture required for comfortable living. This usually includes items such as a bed, couch, TV with satellite channels, Internet solution, dining table and chairs, and standard kitchen appliances."""
    },

    {
        "section": "sta_process_details",
        "content": """Short Term Assignment (STA) Process:
1. The Host Country department head submits the STA request to the Host Country HRBP after granting the approval from the Host Country BU Head.
2. The Host Country HRBP submits the STA form to the Home Country HRBP.
3. The Home Country HRBP confirms the duration and STA end date.
4. The Host Country HRBP requests from the Group Total Rewards to issue the STA offer letter. (All the STA offers must be signed and stamped from the Group Total Rewards).
5. The employee signs the STA offer.
6. The Home and Host countries HRBPs communicates together to facilitate the process.

STA Key Rules:
- The employee should not sign a local contract in the Host country, but if needed to perform the STA tasks in the host country, the host country could issue the required work permit and residency limited to the mission period.
- If the STA exceeded 12 months, the employee must resign or sign UPL form from home country and sign a new contract in the host country abiding by the LTA terms or the localization, at least 2 months prior the STA expiration date – as per the legal Department in coordination with the home and host countries HRBPs after the confirmation of both BUs' Heads."""
    },

    {
        "section": "sta_compensation_benefits",
        "content": """STA Compensation During Assignment:
1. Basic salary, grants, and performance bonus to remain the same as the current home currency.
2. The business performance bonus to be earned as per the host country currency according to its performance prorated to the STA duration.
3. All types of allowances paid in the home country such as transportation and mobile allowances will be held until the end of the STA.
4. A COLA to be paid in foreign currency relevant to their approved grades as per the pay matrix for each country. COLA to be paid till the end of the assignment and to be stopped once the employee returns to the home country.
5. In case the assigned employee returned to the home country for any reason during the STA for 1 month or more, The STA allowances will be stopped until returning to the host country.
6. The assigned employee is not allowed to return to the home country on annual leaves before 3 months from the STA start date. Leave days subject to the home country labor law, prorated to the STA duration.
7. The BU will cover the housing including the utilities, ensuring it's a furnished unit in a safe place, nearby the airport and the facilities area.
8. The BU will cover the transportation and car allowances (if applicable) as per the table of benefits of each country relevant to the employee's approved grade.
9. The company to provide minimum 1 and maximum of 2 round trips during the one-year STA period, from the host country to the home country and vice versa. (Flight class depends on the grade as per the travel policy).
10. The company does not cover the cost of accompanying family members.
- The Medical insurance will remain active as is in the home country.
- The medical insurance services are covered 100% by the host country/BU for the assigned employee during the STA either through a local medical insurance company or invoices reimbursements after the group doctor's approval."""
    },

    {
        "section": "lta_process_details",
        "content": """Long Term Assignment (LTA) Process:
The long-term assignments require the employee to travel from 1 year to a maximum of 2 years in key roles within the host country. The primary objectives of this rotational approach are to facilitate knowledge sharing, develop global leadership capabilities, and enhance employee retention.

LTA Process Steps:
1. The Host Country department head submit the LTA request to the Host Country HRBP.
2. The Host Country HRBP submit the request to Group Internal Mobility (IM) (Group.IM@elsewedy.com)
3. Group IM posts the vacancy internally.
3. Sector TM proactively lists the HIPOs and Watch-listers for the sector.
4. Sector TM check if any of the global open vacancies is suitable for the HIPOs and watch-listers list to be filled from within the group.
5. Sector TM nominate the matched employees to Group IM after granting the line manager confirmation.
6. Group IM send the nominated list to the Host Country HRBP after validation.
7. The Host country HRBP and line manager interview the nominated employee.
8. The Group IM request from the Group Total Rewards to issue the offer letter. (All the offers must be signed and stamped by the Group Total Rewards)
9. The employee to sign an unpaid leave document in the home country and a new localized temporary contract will be issued by the host country's HRBP under the new legal entity/country BU as per the new country's law and regulated by the Group Legal department.

LTA Key Requirements:
- This Term requires close collaboration between Group & Sector Talent Management, Group Internal Mobility, and Group Organization Design to identify suitable candidates and destinations based on the talent plans designed by Group TM and executed by Sector TM.
- All bands are entitled to long term assignment (LTA) terms except for leadership band.
- The home country BU is responsible to secure for the employee his/her current job during the LTA."""
    },

    {
        "section": "localization_process",
        "content": """Localization Term Process:
The business trip that requires the employees to travel permanently is categorized as Localization. It necessitates the employee to exist physically more than 12 months in the host country with a host country local contract.

Localization Process Steps:
1. The Host Country department head submits the request to the Host Country HRBP.
2. The host country's HRBP notifies the Group Internal Mobility (Group.IM@elsewedy.com) with the hiring request after the confirmation of the host country's BU head.
3. The Group Internal Mobility validates with Group Organization Design the position and its grade.
4. The Group Internal Mobility communicates with the home country HRBP for the selected employee's transfer.
5. The Home Country HRBP aligns the department head regarding the employee transfer.
6. The Group Internal Mobility requests from the Group Total Rewards to issue the localization offer letter. (All the offers must be signed and stamped from the Group Total Rewards)
7. The Localized employee contract will be ended from the home country, and a new contract will be issued by the host country's HRBP under the new legal entity/country BU as per the new country's law and regulated by the Group Legal department."""
    },

    {
        "section": "localization_compensation",
        "content": """Localization Compensation:
- A lumpsum one-off amount to be paid in advance to facilitate the employee relocation with a minimum of 1 month up to 3 months from his new basic salary to be deducted on a monthly basis over 6 months.
- All pay elements including the accommodation, transportation and car allowances (if applicable) must be fully paid in the defined host country currency relevant to the approved grades, and as per the country salary structure & benefits scheme.
- All benefits like bonus, grants, leaves, etc... will be based on the local contract as per the host country's rules and regulations.
- In case the employee accompanied his/her family: The family relocation must be at least after 6 months from the employee transfer date. The employee will bear the cost of their relocation, visa, residence, etc… yet the employer might help him in the relocation operations.
- The host company will provide a maximum of 2 round trips per year for the employee, If the employee is accompanied by family, only 1 round trip ticket for him/her and for each family member up to "three accompanying per year" taking into consideration the host country's process and table of benefits.
- Education assistance will be provided to the management band and above for specific countries upon the local practices, this is applicable if the employee is accompanied by their family, and they are officially residents in the host country.
- Education assistance to be covered by the BU and reimbursed against paid invoices as per the market trends for each country to be defined by the Group Total Rewards.
- The medical insurance will be covered by the host country as per the local policy.
- If the employee's family remains in home country, the home country medical insurance will be cancelled for him and his family."""
    },

    {
        "section": "blue_collars_mobility",
        "content": """Blue Collars Mobility Process:
1. The Host Country department head submits the request to the Host Country HRBP.
2. The host country's HRBP notifies the Group Internal Mobility (Group.IM@elsewedy.com) with the hiring request after the confirmation of the host country's BU head.
3. The Group Internal Mobility communicate with the home country HRBPs for nominations conditioning their performance appraisals result is at least Meets exceptions
4. The Group Internal Mobility develop a technical committee to assess the blue collars' capabilities. "the committee must include Host countries HRBPs, technical expert, host country line manager, and group IM responsible person"
5. The committee with the Group IM decides the BC who will travel whether on LTA or localization."""
    },

    {
        "section": "general_rules_principles",
        "content": """General Rules & Principles:
- The host country will provide comprehensive support to the employee, including work permit, assistance with housing and cultural orientation.
- If employee will be transferred to a higher Job with higher grade, the Internal Mobility / promotion policy criteria should take place in prior.
- All global mobility offers to be issued, signed & stamped from the Group Total Rewards and signed by the Group CHRO and CEO.
- The host country's HRBP in case of the LTA and Localization terms should follow on the below criteria before submitting the request to the global internal mobility:
  o Approved organization structure. The organization structure, to be approved by the Group Organization Design Team prior the communication with the Group Internal Mobility.
  o Available job at the requested grade. The jobs to be evaluated by the Group Total Rewards Team."""
    },

    {
        "section": "rectification_situations",
        "content": """Rectification of the situation: Employees who relocated from their home country (the country where they were hired originally in ELSEWEDY ELECTRIC Group). The following actions need to take place maximum by 15th of May 2025:

For Employees who travelled after the 1st of July 2024:
- In case of STA: Decide the end of mission (STA) date which should not exceed 12 months from the STA start date and the employee to sign a letter of assignment if he/she didn't sign one.
- In case of LTA: the employee to sign unpaid leave document in the home country and a temporary local contract in the host country.
- In case of Localization: If the end of mission date is not determined, the employee must resign from the home country immediately and sign a local term contract at the host country.

For Employees who travelled before the 1st of July 2024:
- In case of STA: Employee who didn't sign a local contract and a decision has been made to get back to the home country, the employee must return immediately to the home country with a notice/grace period of 2 months maximum.
- In case of LTA: the employee to sign unpaid leave document in the home country and a temporary local contract in the host country taking into consideration the LTA period doesn't exceed the 2 years.
- In case of Localization: Employee who signed a local term contract and there is a business need for their physical existence in the host country, they must resign immediately from the home country. Employee who didn't sign a local term contract and there is a business need for their physical existence in the host country, they must resign immediately from the home country and sign a local term contract in the host country.

For Employees returning to their home country with an active contract, it's the BU's responsibility to provide a proper full-time job for the employee as per the BU's approved organization structure as long as they are not low performers and will be required to leave."""
    },

    {
        "section": "rectification_stakeholders",
        "content": """The Rectification Stakeholders: Engaging rectification stakeholders is crucial for effective problem solving and ensuring that corrective measures are sustainable and accepted. The full exercise is owned by the home country BU Head & HRBP with the involvement of the host country BU Head & HRBP, and the employee."""
    },

    {
        "section": "benefits_table_sta",
        "content": """Short-Term Assignment (STA) Benefits (30 days up to 1 Year):
- Basic Salary: Basic Salary will be fully paid from the Home country based on the Job level and as per the Salary Structure
- COLA (cost of living allowance): An amount to cover the cost of living variance based on Cost of living Index.
- Hardship & Hazard Allowance: For Countries that require allowance due to Danger or Hard living conditions
- Company Car: N/A
- Transportation Allowance: Amount to cover the Transportation allowance from to Work location - eliminated if company provide transportation or a car that includes all expenses
- Mobile Allowance: Allowance to be provided to cover the business calls expenses based on Job level and Job nature.
- Education Assistance Allowance: N/A
- Housing Allowance & Accommodation: The company to provide housing - 1 bedroom - Furnished apartment in safe area and near the project. A lumpsum amount could be paid in advance to facilitate the employee relocation with a maximum of three month from his new basic salary.
- Performance Bonus: Paid based on basic salary and as per local (Home) company policy
- Airline Tickets: The company will provide a maximum of 2 round trips economy class during the one-year mission period, from the host country to the home country and vis versa"""
    },

    {
        "section": "benefits_table_lta_localization",
        "content": """Localization/Long-Term Assignment (LTA) Benefits:
- Basic Salary: Basic Salary will be fully paid from the Host country based on the Salary structure & Market pay
- COLA (cost of living allowance): N/A
- Hardship & Hazard Allowance: For Countries that require allowance due to Danger or Hard living conditions
- Company Car: As per local company policy in the Country, Based on Job level or the Job Nature
- Transportation Allowance: Amount to cover the Transportation allowance from to Work location - eliminated if company provide transportation or a car that includes all expenses
- Mobile Allowance: As per local company policy in the Country, Based on Job level or the Job Nature
- Education Assistance Allowance: Education assistance will be provided to the management band and above for the GCC Countries only. For maximum 2 Kids with annual amount of 10K USD each or in the equivalent Host currency.
- Housing Allowance & Accommodation: A lumpsum amount could be paid in advance to facilitate the employee relocation with a maximum of 1 month up to 3 months from his new basic salary.
- Performance Bonus: Paid based on basic salary and as per local (Host) company policy
- Airline Tickets: The company will provide a maximum of 2 round trips economy class per year for the employee, If the employee is accompanied by family only 1 round trip tickets for up to three accompanying."""
    },

    {
        "section": "policy_compliance_discipline",
        "content": """Policy Compliance: Elsewedy Electric may conduct regular audits in all its facilities and structures to monitor compliance with this policy. The Group could also conduct internal surveys or initiatives to encourage the employees to always report violations of its policies. All concerns related to the policy shall be freely raised and appropriately handled and followed up by the Group.

All Elsewedy Electric staff members are expected to report any case of non-compliance with the policy. The employees should be aware that they have a moral and ethical duty to report such instances and should not fear retaliation. The Group recognizes the importance of confidentiality and could grant anonymity to the complainants who wish so, given that such information does not impede the investigation or resolution of the dispute. There should be no limitation to the filing of complaints, in terms of accessibility to all employees and quantity. The Group will make sure that the employees know where and to whom they can refer for denounces or complaints. Elsewedy Electric ensures that appropriate measures and penalties will be applied in case of non-compliance with this policy.

Discipline & Remediation: Violations of this policy may lead to disciplinary action up to, and including, termination of employment/partnership. All disciplinary actions shall be undertaken in accordance with the Group's sanctions list and with all applicable local laws and other legal requirements. The remediation shall be undertaken on a case-by-case basis and in accordance with all applicable local laws and other legal requirements.

Policy Review: This policy shall be reviewed annually and/or when deemed necessary."""
    }
],

[
    {
        "section": "Policy Overview",
        "content": "Exceptional Loan Policy. To set a standard system for employees' exceptional loans in El Sewedy Electric Group, as the group aims at alleviating the employees' burdens in emergency cases."
    },
    {
        "section": "Scope",
        "content": "El Sewedy Electric companies in Egypt."
    },
    {
        "section": "Responsible Employees",
        "content": "BU GM / MD / CEO. Finance Managers. HR Managers. Dept. Managers."
    },
    {
        "section": "Exception Cases Definition",
        "content": "Exceptions cases: 1-Marriage (the employee or their children). 2- Disasters (Home fire, earthquakes, house collapses, accidents). 3- Hajj."
    },
    {
        "section": "Marriage Loan - Employee",
        "content": "1-Marriage. Loan in case of employee marriage. It is eligible for dispensing once. The employee or worker must complete a period of three years of work in Elsewedy companies; the maximum loan limit is 50,000 EGP or four times the salary, whichever is higher, to be installed for a maximum of 36 months. The employee should submit the marriage certificate."
    },
    {
        "section": "Marriage Loan - Children",
        "content": "Loan in case of marriage of employees' children. It is eligible for dispensing three times. The employee or worker has to complete a period of five years of work in Elsewedy companies and should not pay for any previous loans. The maximum loan limit is 50,000 EGP or four times the salary, whichever is higher, to be installed for 36 months or until retirement age. The employee should submit the marriage certificate to his children."
    },
    {
        "section": "Disasters Loan",
        "content": "2- Disasters (Home fire - earthquakes - house collapses - accidents). It is eligible for dispensing once. The employee or worker has to complete a period of five years of work in Elsewedy companies; the maximum loan limit is 50,000 EGP or four times the salary, whichever is higher, to be installed for a maximum of 36 months or until retirement age whichever comes first. A committee is formed to examine cases of disasters and submit case reports to the HR Department."
    },
    {
        "section": "Hajj Loan",
        "content": "3-Hajj (the employee himself). It is eligible for dispensing once. The employee or worker has to complete a period of ten years of work in Elsewedy companies; the maximum loan limit is 50% of the value of economic Hajj which announced by the ministry of tourism to be installed for a maximum of 36 months or until retirement age, and the employee must submit documents proving that he or she has performed Hajj."
    },
    {
        "section": "General Principles - Eligibility",
        "content": "An employee who has spent the period of work that exists under the conditions of the exceptional loan cases within Elsewedy companies has the right to request an exceptional loan, provided that it does not exceed four months' salary or the amount specified for each case, whichever is higher."
    },
    {
        "section": "General Principles - Previous Loans",
        "content": "The employee must have fully paid the previous exceptional loan before requesting any new loan, and three years have passed since the date of the previous loan. It is also required that there be 2 paid guarantors who have served for a period not less than two years."
    },
    {
        "section": "General Principles - Guarantors",
        "content": "One guarantor can grant a maximum of 2 employees. The guarantors will repay the loan in the case that the employee is unable to pay it."
    },
    {
        "section": "General Principles - Documentation",
        "content": "The employee who can't submit the required proof isn't eligible for any loans."
    },
    {
        "section": "General Principles - Termination",
        "content": "In case of termination of the employee's contract for any reason, the amount of the loan shall be deducted at once."
    },
    {
        "section": "General Principles - Total Limit",
        "content": "The total approved exceptional loans balance mustn't exceed 5% of the company's total annual salaries."
    },
    {
        "section": "Procedures - Application",
        "content": "The employee makes an application for an exceptional loan, specifying the required amount so that it does not exceed four months' salary or the amount specified for each loan, whichever is higher. The form includes the signatures of 2 guarantors, explaining the reason for the loan and stating the installment period."
    },
    {
        "section": "Procedures - Manager Approval",
        "content": "An employee must submit the form to his/ her direct manager for approval, being sure of the guarantors' signatures and the reason of the loan."
    },
    {
        "section": "Procedures - HR Review",
        "content": "An employee must submit the form to the HR Dept. for revision in accordance with the above-mentioned terms and conditions and for GM/ CEO approval."
    },
    {
        "section": "Procedures - Final Processing",
        "content": "Then the loans are approved and grouped into one statement. HR Dept. shall coordinate with Finance to provide the required amount of loan, hand it over to the employee, and deduct the monthly installments from his or her next salary over a maximum period of 36 months."
    },
    {
        "section": "Required Documents",
        "content": "A loan request with the signatures of the employee, guarantors, and direct manager states the amount of the requested loan, installment period and the loan reason. The employee's signature on a trust receipt for the amount."
    },
    {
        "section": "Exemption",
        "content": "The exemption is made in the case of death or total disability."
    }
],

[
    {
        "section": "عنوان السياسة",
        "content": "سياسة سلف العاملين الاستثنائية. وضع نظام موحد لسلف العاملين الاستثنائية بمجموعة شركات السويدي الكتريك حيث تهدف المجموعة إلى المشاركة في تخفيف العبء عن العاملين في الظروف الطارئة."
    },
    {
        "section": "نطاق التطبيق",
        "content": "شركات السويدي الكتريك داخل جمهورية مصر العربية"
    },
    {
        "section": "المسئولين",
        "content": "مدير عام الشركة. المديرين الماليين. مديري الموارد البشرية. مديري الإدارات."
    },
    {
        "section": "حالات الاستثناءات",
        "content": "1-الزواج (الموظف أو الأبناء). 2-الكوارث (حريق المسكن-الزلزال-انهيار المنازل-الحوادث). 3-الحج."
    },
    {
        "section": "الزواج-سلفة في حالة زواج الموظف نفسه",
        "content": "يتم صرفها مرة واحدة بشرط أن يكون الموظف أو العامل قد أجتاز فترة ثلاثة أعوام عمل في شركات السويدي وأقصي حد للسلفة 50,000 جنيها أو أربعة أضعاف الراتب أيهما أعلي على أن يتم سدادها علي 36 شهرا بعد أقصي او بغرض تقديم قسيمة الزواج."
    },
    {
        "section": "سلفة في حالة زواج أبناء العاملين",
        "content": "يتم صرفها لمدة حد أقصي ثلاثة مرات بشرط مضد السلفة السابقة وأن يكون الموظف أو العامل قد اجتاز فترة خمسة أعوام عمل في شركات السويدي وأقصي حد للسلفة 50,000 جنيها أو أربعة أضعاف الراتب أيهما أعلي على أن يتم دفعها علي 36 شهرا بعد أقصي أو حتى سن المعاش ، و بشرط تقديم قسيمة الزواج للأبناء."
    },
    {
        "section": "الكوارث",
        "content": "(حريق المنزل-انهيار المنازل-الحوادث). يتم صرفها مرة واحدة بشرط أن يكون الموظف أو العامل قد اجتاز فترة خمسة أعوام عمل في شركات السويدي وأقصي حد للسلفة 50,000 جنيها أو أربعة أضعاف الراتب أيهما أعلي على أن يتم دفعها علي 36 شهرا بعد أقصي أو حتى سن المعاش أو حتى سن المعاش أيهما أقرب. يتم تشكيل لجنة لبحث الحالات الخاصة بالكوارث لتقديم تقارير الحالات لإدارة الموارد البشرية."
    },
    {
        "section": "الحج (الموظف نفسه)",
        "content": "يتم صرفها مرة واحدة بشرط أن يكون الموظف أو العامل قد اجتاز فترة عشر أعوام عمل في شركات السويدي وأقصي حد للسلفة 50% من تكلفة الحج الاقتصادي (الأرخص العامل من وزارة السياحة علي أن يتم دفعها علي 36 شهرا بعد أقصي أو حتى سن المعاش ، و بشرط تقديم المستندات الدالة علي قيام الموظف بالحج."
    },
    {
        "section": "المبادئ العامة",
        "content": "يحق للموظف الذي يكون قد اجتاز فترة العمل الموجودة في شروط السلف الاستثنائية داخل شركات السويدي أن يطلب سلفة استثنائية بحيث لا يجاوز راتب أربعة أشهر أو المبلغ المحدد لكل حالة أيهما أعلي."
    },
    {
        "section": "شرط تسديد السلف السابقة",
        "content": "يشترط تسديد الموظف السلفة الاستثنائية السابقة قبل طلب أي سلفة جديدة وأيضا مرور 3 سنوات من تاريخ السلفة السابقة كما يشترط وجود عدد 2 ضامنين علي أن لا تقل مدة عملهم عن سنتان."
    },
    {
        "section": "الضامنين",
        "content": "يستطيع الضامن الواحد أن يضمن \"2\" موظفين بعد أقصي. في حالة عجز الموظف عن سداد السلفة سيقوم الضامنين بسداد السلفة نيابة عنه."
    },
    {
        "section": "المستندات المطلوبة",
        "content": "عند عجز الموظف عن تقديم الإثباتات المطلوبة لا يحق له الحصول علي أي سلفة."
    },
    {
        "section": "إنهاء الخدمة",
        "content": "في حالة انتهاء خدمة الموظف لأي سبب من الأسباب يتم خصم مبلغ السلفة دفعة واحدة."
    },
    {
        "section": "إجمالي السلف",
        "content": "إجمالي السلفة الاستثنائية التي يتم اعتمادها يجب ألا يتجاوز رصيدها في بداية الشهر %5 من إجمالي مرتبات الشركة كل في السنة."
    },
    {
        "section": "الإجراءات",
        "content": "يقوم الموظف بتحرير نموذج طلب السلفة الاستثنائية محددا فيه المبلغ المطلوب بحيث لا يتجاوز راتب أربعة أشهر أو المبلغ المحدد لكل سلفة أيهما أعلي، ويتضمن النموذج توقيع ضامنين مع توضيح سبب السلفة وتحديد فترة التقسيط."
    },
    {
        "section": "اعتماد المدير",
        "content": "يقوم الموظف بتقديم الطلب إلى المدير المباشر لاعتماده والتأكد من توقيع الضامنين وسبب السلفة."
    },
    {
        "section": "مراجعة الموارد البشرية",
        "content": "يقوم الموظف بعد اعتماد المدير المباشر بتقديم الطلب لإدارة الموارد البشرية التي تقوم بمراجعة الطلب طبقا للشروط المذكورة واعتماده من مدير عام الشركة."
    },
    {
        "section": "المعالجة النهائية",
        "content": "يتم اعتماد السلف مجمعة في بيان واحد. تقوم إدارة الموارد البشرية بالتنسيق مع الإدارة المالية لصرف مبلغ السلفة وتسليمه للموظف وتقوم بخصم الأقساط الشهرية من راتب الموظف من الشهر التالي للصرف بحد أقصى 36 شهرا."
    },
    {
        "section": "الأوراق المطلوبة",
        "content": "طلب السلفة مع إمضاء الموظف والضامنين والمدير المباشر موضح به مبلغ السلفة المطلوبة ومدة التقسيط وسبب السلفة. توقيع الموظف على إيصال أمانة بالمبلغ."
    },
    {
        "section": "الإعفاء",
        "content": "يتم الإعفاء في حالة الوفاة أو العجز الكلي لا قدر الله."
    }
],

[
    {
        "chunk_id": "purpose_applicability",
        "section": "Purpose and Applicability",
        "content": """Purpose: To set, define and communicate broadly Elsewedy Electric policy concerning promotions ensuring equal opportunity to all employees based on job evolution, performance, and business need. This Policy is a minimum standard; where local legislations define higher standards; the Group shall comply with them.

Applicability: This policy applies to all the operating companies and subsidiaries directly or indirectly controlled by Elsewedy Electric, and all the geographical regions where Elsewedy Electric companies and subsidiaries are operating."""
    },

    {
        "chunk_id": "9_box_grid_overview",
        "section": "The 9-Box Grid of Talent Differentiation",
        "content": """The 9-Box Grid of Talent Differentiation is a tool used during the TRM (Talent Review Meeting) to measure the (potentiality) of the employees in comparisons to each other (within the same band) based on the 3 last year's performance and capabilities scores. The output of the grid is used to take the Talent Management decisions and design the relevant programs. The Talent Review Meetings (TRM) are led by the Sector/BU HRBP with the Sector/BU Head and the Sector/BU Management Team. A TRM for a specific band is expected to last for 60-90 mins for each of the 4 Bands."""
    },

    {
        "chunk_id": "promotion_definitions",
        "section": "Promotion Definitions",
        "content": """Promotion is any upward movement of an eligible employee to a higher role that requires more responsibilities and consequently additional competencies. There are two types of promotions:

Grade Promotion is an upward move within the same band. Please refer to the grading and titling matrix.

Band Promotion is an upward move from one band to another. Please refer to the grading and titling matrix."""
    },

    {
        "chunk_id": "high_potential_definition",
        "section": "High Potential (HiPo) Definition",
        "content": """A nominated High Potential (HiPo):
• Is an employee who is identified by the Sector/BU TRM to have a high possibility to move up the grading ladder.
• A nominated HiPo employee is entitled to be enrolled into the Group TAC (Talent Assessment Center) for confirmation.
• The nominated HiPo employee who successfully passes the Group TAC is considered as a confirmed HiPo (ready now) and is entitled for a band promotion subject to job availability and budget.
• If the nominated HiPo fails to pass the TAC, the employee moves to the Watch-Listers boxes."""
    },

    {
        "chunk_id": "tac_definition",
        "section": "Group Talent Assessment Center (TAC)",
        "content": """The objective of the TAC is to make sure that the employee meets the requirement for the next role in terms of:
1. Core and Leadership Competencies.
2. Abilities.
3. Work preferences and values.
4. Aspiration and willingness for new responsibilities.

While the following attributes are measured and confirmed prior to the TAC by the Sector/BU HRBP and Department's Head post the TRM:
1. Cross-functional knowledge. By the business
2. Technical know-how and skillset. By the business
3. Education. By the business
4. Depth and breadth of experience. By the business"""
    },

    {
        "chunk_id": "tac_results_communication",
        "section": "TAC Results Communication",
        "content": """The results of the TAC are communicated through the Group Organization Design Team to the Sector/BU HRBP. The brief of the TAC for the (Senior Management) and (Leadership) bands, are communicated through the Group Talent Management Team directly to the employee in the presence of the Sector/BU HRBP and the Sector Talent Management. For the rest of the bands, the brief of the TAC is communicated to the employee through the Sector/BU HRBP and the Sector Talent Management."""
    },

    {
        "chunk_id": "watch_lister_definition",
        "section": "Watch-lister Definition",
        "content": """A Watch-lister:
• Is an employee who is identified by the Sector/BU TRM to be (ready within 1-2 years) for a band promotion and therefore for being nominated HiPo in 1-2 years.
• A Watch-lister readiness can be accelerated through the Leadership Academy, Functional Academies, … and other development programs.
• A Watch-lister is entitled for a grade promotion within the same band, but not a band promotion which is exclusively offered for confirmed HiPo employees only."""
    },

    {
        "chunk_id": "key_talent_definition",
        "section": "Key Talent Definition",
        "content": """A Key Talent:
• Is an employee who is meeting expectations for his/her current job.
• Key Talent, box 5, at any band can be promoted to higher grade within the same band."""
    },

    {
        "chunk_id": "band_promotion_process",
        "section": "Band Promotion Process",
        "content": """TAC is required in promotion from band to another.

1. The Line Manager nominates and submits the promotion requests for Department's Head approval using the (Promotion Request Form).
2. The Department Head approves and submits the form to the Sector/BU HRBP.
3. The Sector/BU HRBP reviews and approves the promotion requests based on the following 5 promotion criteria:
   ✓ Approved organization structure. The organization structure, to be approved by the Group Organization Design Team prior the promotion round start date.
   ✓ Available job at the requested grade. The jobs to be evaluated by the Group Total Rewards Team.
   ✓ Available budget. The Sector/BU HRBP to make sure not to exceed the personnel cost versus the sales revenue ratio budget set for the year.
   ✓ The readiness of the nominated employee. Employees entitled for a band promotion are only the confirmed HiPo employees and Watch-listers in case there are no HiPos.
   ✓ Approval of the Sector/BU Head."""
    },

    {
        "chunk_id": "band_promotion_validation",
        "section": "Band Promotion Validation Process",
        "content": """4. The Sector/BU HRBP submits the promotion list to the Group Organization Design Group.OD@elsewedy.com for validation and final confirmation.

In case of a support function job, the Group Organization Design submits the promotion nominations to the Group Support Departments HRBP to grant the confirmation from the Group Support Department's Head. Group Support Departments in scope are Finance, Human Resources, Information Technology, Legal, Audit & Compliance, and the Marketing.

In case of Leadership band jobs, the approval must be granted from the Group CHRO followed by the Group CEO.

5. Once validated and confirmed, the Sector/BU HRBP shares the confirmed promotions' list with the Sector/BU Head and announces the promotions to the Head of Departments, promoted employees and their Line Managers. Approved promotions are effective April payroll for cycle 1 and October payroll for cycle 2."""
    },

    {
        "chunk_id": "band_promotion_notes",
        "section": "Band Promotion Additional Notes",
        "content": """Note:
• If the business has a vacancy and does not have a confirmed HiPo for the job within the Sector/BU, it is highly recommended to look for a confirmed HiPo in a sister company within Elsewedy electric Group. The Sector/BU HRBP and the Sector Talent Management to reach out to the Group Internal Mobility Team group.im@elsewedy.com to advise the availability of suitable talent(s).
• In case there is no suitable talent(s) outside, it is accepted that the business looks for a Watch-Lister inside the Sector/BU. The Sector/BU HRBP nominates the candidate for a TAC.
• The promoted HIPO, in case of a band promotion, will be placed in the Key Talent Box for his new role as illustrated in the below figure."""
    },

    {
        "chunk_id": "grade_promotion_process",
        "section": "Grade Promotion Within Same Band Process",
        "content": """1. The Line Manager nominates and submits the promotion requests for Department's Head approval using the (Promotion Request Form).
2. The Department Head approves and submits the form to the Sector/BU HRBP.
3. The Sector/BU HRBP reviews and approves the promotion requests based on the following 5 promotion criteria:
   ✓ Approved organization structure. The organization structure, to be approved by the Group Organization Design Team.
   ✓ Available job at the requested grade. The jobs to be evaluated by the Group Total Rewards Team.
   ✓ Available budget. The Sector/BU HRBP to make sure not to exceed the personnel cost versus the sales revenue ratio budget set for the year.
   ✓ The readiness of the nominated employee. Confirmed HiPo has the priority, Nominated HiPo, Watch-Listers and key talents are entitled for a grade promotion within the same band.
   ✓ Approval of the Sector/BU Head."""
    },

    {
        "chunk_id": "grade_promotion_validation",
        "section": "Grade Promotion Validation Process",
        "content": """4. The Sector/BU HRBP submits the promotion list to the Group Organization Design Group.OD@elsewedy.com for validation and final confirmation.

In case of a support function job, the Group Organization Design submits the promotion nominations to the Group Support Departments HRBP to grant the confirmation from the Group Support Department's Head. Group Support Departments in scope are Finance, Human Resources, Information Technology, Legal, Audit & Compliance, and the Marketing.

In case of Leadership band jobs, the approval must be granted from the Group CHRO followed by the Group CEO.

5. Once validated & confirmed, the Sector/BU HRBP shares the confirmed promotions' list with the Sector/BU Head and announces the promotions to the Head of Departments, promoted employees and their Line Managers. Approved promotions are effective April payroll for cycle 1 and October payroll for cycle 2."""
    },

    {
        "chunk_id": "basic_principles_eligibility",
        "section": "Basic Principles - Eligibility and Timing",
        "content": """• Eligibility for promotion is not by any means related to spending several years in a specific job.
• An increase in job duties within a job level does not normally necessitate a promotion at an individual's level.
• The Sector/BU HRBP to make sure not to exceed the personnel cost versus the sales revenue ratio budget set for the year.
• Fast track for the confirmed HiPos allow them to be promoted either band to band or grade to grade after 1 year from the last promotion date."""
    },

    {
        "chunk_id": "basic_principles_timing_restrictions",
        "section": "Basic Principles - Promotion Timing Restrictions",
        "content": """• Employees on the Senior Professional band and above shall not be considered for another promotion for a period of two years from the last promotion date/joining date. However; from M3 to M2, the employee can be promoted after 1 year conditioning his talent review is Key Talent or above.
• Employees on the Professional band shall be considered for another promotion for a period of one year from the last promotion date/joining date on condition to being identified as HiPo or watch lister, otherwise will be eligible after 2 years from last promotion date.
• The GDP employees shall be promoted after passing the GDP year during the nearest promotion cycle (from P3 to P2) in condition to being identified as a key Talent/(Performance appraisal at least Meeting expectations)."""
    },

    {
        "chunk_id": "basic_principles_budget_contract",
        "section": "Basic Principles - Budget and Contract Considerations",
        "content": """• It is highly recommended to allocate 1% extra budget in the payroll to accommodate the promotions' cost.
• In case of annual contract renewal, if the promotion request is approved, then the new job title should be included in the new contract upon annual renewal."""
    },

    {
        "chunk_id": "basic_principles_restrictions",
        "section": "Basic Principles - Employee Restrictions",
        "content": """• Employees who are on unpaid leave are not eligible for promotion.
• Employees who have submitted their resignation and on notice period are not eligible for promotions. This means that promotion cannot be used as a retention tool for reigned employees.
• Employees under formal investigation through an official committee are not eligible for promotion.
• Employees who have received warning letters or any disciplinary action during the previous 24 months are not eligible for promotion."""
    },

    {
        "chunk_id": "grading_matrix_leadership",
        "section": "Grading Matrix - Leadership and Senior Management",
        "content": """Leadership Band:
- CEO: Group CEO
- L1: Group Vice President
- L2: Sector CEO, Group C Level A
- L3: Managing Director, Group C Level B

Senior Management Band:
- D1: General Manager, Group Director, Sector Director
- D2: Director A
- D3: Director B"""
    },

    {
        "chunk_id": "grading_matrix_management_professional",
        "section": "Grading Matrix - Management and Professional",
        "content": """Management Band:
- M1: Senior Manager
- M2: Manager A
- M3: Manager B

Senior Professionals Band:
- S1: Section Head
- S2: Team Leader, Executive Assistant A

Professionals Band:
- P1: Senior Engineer, Executive Assistant B
- P2: Engineer, Specialist
- P3: Junior Engineer, Assistant Coordinator, Department Assistant

Technicians & Workers Band:
- T1: Supervisor, Foreman
- T2: Senior Technician, Driver St
- T3: Assistant, Technician, Driver Gr
- T4: Assistant Technician, Worker"""
    }
],

[
    {
        "chunk_id": 1,
        "section": "Policy Overview",
        "content": "Salary Adjustment Exercise Policy. Purpose: To ensure fair and consistent salary adjustments for all employees, reflecting their Talent review, market conditions, and the company's financial health. Scope: This policy applies to all Elsewedy Electric full-time employees. Adjustment Cycle: Salary adjustments will occur twice a year, in April and October."
    },

    {
        "chunk_id": 2,
        "section": "Entitlement Criteria",
        "content": "Entitlement: Employees who are entitled for a salary adjustment are the employee who -as per the 9-Box Grid of the Talent Differentiation- are in the following positions: High Potentials Box 9, Watch-Listers, Box 8 and 6, Key Talent, Box 5, Quality Performers, Box 3, Quality Talent, Box 7"
    },

    {
        "chunk_id": 3,
        "section": "9-Box Grid Structure",
        "content": "The 9-Box Grid shows performance and potential matrix with the following categories: Box 9 - High Potential (HIPO): To retain and promote. Box 8 and 6 - Watch-lister (WL): To stretch, develop and retain. Box 7 - Quality Talent (QT): Stretch true performance to move into the watch-listers zone. Box 5 - Key Talent (KT): To develop and develop. Box 3 - Quality Performers (QP): Develop their competencies to move into the watch-listers zone. The distribution reflects an example of a BU achieved 100% results over the last 2-3 years"
    },

    {
        "chunk_id": 4,
        "section": "Adjustment Priority",
        "content": "NB: It is crucial to foster applying the salary adjustment for the High Potentials HIPOs and Watch-Listers, thereafter, once moving them to their correct comp-ratio areas and if there's an extra room for adjustments, it goes to the Key Talent, Quality Performers and Quality Talent."
    },

    {
        "chunk_id": 5,
        "section": "Process Step 1-2",
        "content": "Processes: 1. The Sector/BU HRBP to submit the request to the Group Total Rewards (template attached). 2. The Group Total Rewards to revise the submission for approval, considering the following criteria: Employee criteria a. The position of the employee on the 9-box grid b. The current comp-ratio of the employee c. The expected comp-ratio post the submitted proposed increase Cost criteria d. The impact of the total cost of the adjustments approved on the personnel cost e. ratio versus sales revenue (with the Group HR Analytics Team)."
    },

    {
        "chunk_id": 6,
        "section": "Process Step 3-6",
        "content": "3. The Group Total Rewards to reply to the Sector/BU HRBP with one of the following actions: a. Approved. b. Rejected. c. Partially approved. i. either because some employees (cases) do not meet the employee criteria, or ii. The cost criteria are not met. In this case the Group Total Rewards request a modification from the Sector/BU HRBP for a second cycle of submission. 4. The Group Total Rewards to submit to the Group CHRO for review and approval. 5. The Group Total Rewards to submit to Group CEO for the final approval. 6. The Group Total Rewards to send the final feedback to the BU HRBP for implementation."
    },

    {
        "chunk_id": 7,
        "section": "Document Authority",
        "content": "Walid Tayel Group Chief HR Officer"
    }
],

[
    {
        "section": "intro_reminder",
        "content": "As part of our commitment to driving operational excellence, ensuring end-to-end visibility, and avoiding overlapping responsibilities in the hiring process, we would like to remind all teams that TALEO is the single official system to be used for all recruitment actions. No steps should be taken outside the system. This is critical for governance, coordination, and audit purposes."
    },
    {
        "section": "process_overview",
        "content": "Please find below the standard hiring process to be followed for all new and replacement positions:"
    },
    {
        "section": "requisition_phase_intro",
        "content": "(1) Requisition Phase"
    },
    {
        "section": "requisition_steps_1_3",
        "content": "1. Hiring Manager opens the job requisition on TALEO. 2. Head of Department approves the job requisition. 3. Sector/Country Organization Design reviews the business need (especially if unplanned), drafts/revises the Job Description (JD), and proposes the job level."
    },
    {
        "section": "requisition_steps_4_5",
        "content": "4. Group Organization Design validates the BU structure, confirms the need, approves the JD, and performs job evaluation if needed to confirm the proposed level and job title. 5. Group Total Rewards sets the compensation package, including salary range and all other applicable rewards, based on the finalized job level."
    },
    {
        "section": "requisition_steps_6_7",
        "content": "6. BU HRBP reviews and approves the full job requisition and attached details. (in case of an ad-hoc request, not approved in the manpower plan) 7. BU Head gives final approval on the job requisition. (in case of an ad-hoc request, not approved in the manpower plan)"
    },
    {
        "section": "recruitment_phase_intro",
        "content": "(2) Recruitment Phase"
    },
    {
        "section": "recruitment_steps_8_10",
        "content": "8. Recruiter begins the sourcing, screening, and HR interviews. 9. Hiring Manager conducts technical interviews. 10. Recruiter moves the selected candidate to the \"Offering Stage\" on TALEO."
    },
    {
        "section": "recruitment_steps_11_13",
        "content": "11. Group Total Rewards creates the official job offer in the system. 12. Hiring Manager reviews and approves the job offer. 13. BU HRBP approves the job offer."
    },
    {
        "section": "recruitment_steps_14_15",
        "content": "14. BU Head approves the job offer only if the compensation exceeds the range approved by Group Total Rewards. 15. Recruiter officially extends the offer to the candidate via TALEO."
    },
    {
        "section": "important_notes_taleo_logging",
        "content": "All steps must be logged and completed in TALEO — verbal confirmations or through email or Microsoft Teams or What's App or other messaging platforms will not be accepted as formal approvals."
    },
    {
        "section": "important_notes_ownership",
        "content": "The ownership of each step is exclusive to the designated owner listed in the process. No other HR function or business stakeholder is authorized to bypass, replace, or take ownership of a step that is not explicitly assigned to them."
    },
    {
        "section": "important_notes_escalation",
        "content": "Any deviation from this process must be escalated to Group HR Quality Assurance Team group.HRA@elsewedy.com before any action is taken."
    },
    {
        "section": "important_notes_purpose",
        "content": "This structure is designed to ensure alignment, accountability, and speed in the hiring process while maintaining transparency and governance across all functions."
    },
    {
        "section": "contact_signature",
        "content": "Best regards, Group Chief HR Officer"
    }
],

[
    {
        "chunk_id": 1,
        "section": "Purpose",
        "content": "This policy provides guidelines and procedures for all Elsewedy Electric employees eligible for transportation allowances and essential buses or pool cars. It applies to those working in offices or factories and aims to facilitate round trips and business trips from HQ to the main collection points on a daily basis during the working week."
    },
    {
        "chunk_id": 2,
        "section": "Applicability",
        "content": "This policy applies to the Group and all operating companies and subsidiaries directly or indirectly controlled by Elsewedy Electric. Factories and Offices. Geographical Locations: Egypt"
    },
    {
        "chunk_id": 3,
        "section": "Definitions",
        "content": "BUs: is the abbreviation for the Business Units. Eligible Employees: Employees who are allowed to receive a transportation allowance under this policy based on the Table of benefits."
    },
    {
        "chunk_id": 4,
        "section": "Roles and Responsibilities",
        "content": "The following personnel have roles and responsibilities with regard to the implementation of this policy as described in detail in the Principles and Procedures section. Total Reward (Design and Update the policy and review the amounts mentioned in the policy to match the market. HRBP (implementing and approving the Transportation allowance request based on this policy) BU Finance (maintain the Transportation budget based on this policy) CEO/MD/GM (Final approval). The Administration-Fleet Section (Responsible for the transportation facility, operating expenses, and company car maintenance)."
    },
    {
        "chunk_id": 5,
        "section": "Transportation Services Concept",
        "content": "This company should provide a transportation service throughout two concepts: Transportation Services: The company to provide a Transportation facility during normal working hours. Transportation will be available from the main collection/drop-off points at the residence area to the main HQ/Factory/Site as per the defined pick-up time, all set by the Administration Department."
    },
    {
        "chunk_id": 6,
        "section": "Transportation Services - Bus Allocation",
        "content": "Professionals and Senior professionals Bands will share 14 or 25-seat buses. Management Band will share 14-seat bus, especially in the factories area. The same may apply to the Senior Management band if the company does not provide a company car. For work-related trips, the company will provide a car for business meetings, customer visits, supplier visits, bank visits, etc., outside the main office."
    },
    {
        "chunk_id": 7,
        "section": "Transportation Allowance Types",
        "content": "when the company cannot offer a transportation facility, there are two types of transportation Allowance: 1. Transportation allowance: covers commuting costs between the residence area and the main HQ/Factory/Site, based on the Transportation Allowance Benefits Table. 2. Job Transportation allowance: covers business commuting and there are two elements: I. Fixed Transportation Allowance element to cover work-related trips in addition to the regular commute. This allowance is for jobs requiring more than 70% of working hours spent commuting outside the head office, and it is also paid according to the Transportation Allowance Benefits Table. II. Variable Transportation Allowance element to cover only work-related trips paid on actual expense bases."
    },
    {
        "chunk_id": 8,
        "section": "General Principles",
        "content": "The company should provide suitable transportation facilities, which could be buses or pool cars, depending on the company's capability. All buses and pool cars must meet the safety standards defined in the HSE policy. If a department has a car, it should be a pool car available for all employees in that department, not assigned to any specific employee. Employees with Job Transportation Allowance are not entitled to use the pool car. Employees who receive a car based on other benefits policies are not entitled to the Transportation Allowance or the Job Transportation Allowance."
    },
    {
        "chunk_id": 9,
        "section": "Procedures",
        "content": "Each BU to develop its own procedures based on this policy to provide the eligible employees with the Transportation facility or allowance."
    },
    {
        "chunk_id": 10,
        "section": "Policy Compliance",
        "content": "Elsewedy Electric may conduct regular audits in all its facilities and structures to monitor compliance with this policy. The Group could also perform internal surveys or initiatives to encourage the employees to always report violations of its policies. All concerns related to the policy shall be freely raised and appropriately handled and followed up by the Group. All Elsewedy Electric staff members are expected to report any case of non-compliance with the policy. The employees should be aware that they have a moral and ethical duty to report such instances and should not fear retaliation. The Group recognizes the importance of confidentiality and could grant anonymity to the complainants who wish so, given that such information does not impede the investigation or resolution of the dispute. There should be no limitation to the filing of complaints, in terms of accessibility to all employees and quantity. The Group will make sure that the employees know where and to whom they can refer for denounces or complaints. Elsewedy Electric ensures that appropriate measures and penalties will be applied in case of non-compliance with this policy."
    },
    {
        "chunk_id": 11,
        "section": "Discipline and Remediation",
        "content": "Violations of this policy may lead to disciplinary action up to, and including, termination of employment/ partnership. All disciplinary actions shall be undertaken in accordance with the Group's sanctions list and with all applicable local laws and other legal requirements. The remediation shall be undertaken on a case-by-case basis and in accordance with all applicable local laws and other legal requirements."
    },
    {
        "chunk_id": 12,
        "section": "Policy Review",
        "content": "This policy shall be reviewed annually and/or when deemed necessary."
    },
    {
        "chunk_id": 13,
        "section": "Transportation Allowance Benefits Table - Leadership Band",
        "content": "Leadership Band - VP C Level MD: Transportation Allowance 24,000, Job Related Allowance Fixed: Company provides Transportation facility for Specific Jobs. General Manager Group Director Sector Director: Transportation Allowance 18,000, Job Related Allowance Fixed: Company provides Transportation facility for Specific Jobs."
    },
    {
        "chunk_id": 14,
        "section": "Transportation Allowance Benefits Table - Senior Management Band",
        "content": "Senior Management Band - Director A: Transportation Allowance 14,400, Job Related Allowance Fixed: Company provides Transportation facility for Specific Jobs. Director B: Transportation Allowance 14,400, Job Related Allowance Fixed: Company provides Transportation facility for Specific Jobs."
    },
    {
        "chunk_id": 15,
        "section": "Transportation Allowance Benefits Table - Management Band",
        "content": "Management Band - Senior Manager: Transportation Allowance 12,000, Job Related Allowance Fixed: 14,400. Manager A: Transportation Allowance 9,600, Job Related Allowance Fixed: 12,000. Manager B: Transportation Allowance 9,600, Job Related Allowance Fixed: 12,000."
    },
    {
        "chunk_id": 16,
        "section": "Transportation Allowance Benefits Table - Senior Professionals Band",
        "content": "Senior Professionals Band - Section Head: Transportation Allowance 7,200, Job Related Allowance Fixed: 9,600. Team Lead: Transportation Allowance 7,200, Job Related Allowance Fixed: 9,600."
    },
    {
        "chunk_id": 17,
        "section": "Transportation Allowance Benefits Table - Professionals Band",
        "content": "Professionals Band Assistant - Senior Engineer Senior Specialist: Transportation Allowance 6,000, Job Related Allowance Fixed: 8,400. Engineer Specialist: Transportation Allowance 4,800, Job Related Allowance Fixed: 7,200. Junior Engineer GDP Specialist Coordinator: Transportation Allowance 4,800, Job Related Allowance Fixed: 7,200."
    },
    {
        "chunk_id": 18,
        "section": "Transportation Allowance Benefits Table - Technicians and Workers Band",
        "content": "Technicians & Workers Band - Supervisor Foreman: Transportation Allowance 3,000, Job Related Allowance Fixed: 4,200. Senior Technician Driver G1: Transportation Allowance 1,800, Job Related Allowance Fixed: 2,400. Technician Driver G2: Transportation Allowance 1,800, Job Related Allowance Fixed: 2,400. Assistant Technician: Transportation Allowance 1,800, Job Related Allowance Fixed: 2,400."
    },
    {
        "chunk_id": 19,
        "section": "Transportation Benefits Table Note",
        "content": "Based on the Job Nature that needs commuting out side the office, company should provide a transportation facility to the Leadership & Senior Management Team"
    }
],

[
    {
        "section": "purpose",
        "title": "Purpose",
        "content": """This policy aims to:
• Provide guidelines and establishes procedures for all employees at Elsewedy Electric Group incurring business travel and hospitality expenses. All employees are required to comply with these guidelines to receive reimbursement for any expense claims related to travel and hospitality.
• Ensure all business travelers and employees have a clear and consistent understanding of policies and procedures for business travel and hospitality.
• Provide guidance regarding what expense types are, and are not, allowed while traveling or providing hospitality.
• Provide business travelers and employees with a reasonable level of service, comfort and security at the optimum cost.
• Maximize the ability to negotiate discounted rates with suppliers and reduce travel and related expenses, including the utilization of:
1. The Corporate Credit Card Program.
2. The Contracted Airlines (Corporate deals).
3. The Contracted Hotels (Corporate deals).
4. The Contracted Ground Transportation Suppliers.
• Ensure that all authorized expenditures meet and comply with all requirements for tax and expense treatment.
• This policy is a minimum standard; where local legislations define higher standards; the Group shall comply with them."""
    },
    {
        "section": "applicability",
        "title": "Applicability",
        "content": """This policy applies to the Group and all operating companies and subsidiaries directly or indirectly managed by Elsewedy Electric.
✓ Factories
✓ Offices
✓ Engineering, Procurement & Construction Projects
✓ Infrastructure Investments

Geographical Locations:
Africa, America, Asia, Egypt, Europe, GCC, Oceania."""
    },
    {
        "section": "definitions",
        "title": "Definitions",
        "content": """Number of days | Type
1 day – 30 Calendar Days | Business Trip
> than 30 Calendar Days – up to 6 months | Mission
More than 6 months – up to 3 years | Expatriation Term
More than 3 years | Localization Term "Full Transfer"

• BU Head: the GM or the MD of a BU or the CEO of a business sector.
• Frequent travelers: Employees usually traveling more than 6 business trips per Year.
• Standard Room: Basic Room with the main requirements and fundamentals without extra options or any add-ons."""
    },
    {
        "section": "roles_responsibilities",
        "title": "Roles & Responsibilities",
        "content": """The following personnel have roles and responsibilities regarding the implementation of this policy as described in detail in the Principles and Procedures section:
• Traveler: to submit the travel request through the Corporate Travel System (EBP)
• Line Manager: to approve the travel request.
• Corporate Travel Department: to issue the visit visa, book the flight tickets and hotel relevant to the traveler work level with the best prices available (refer to the attached table of benefits)
• BU Finance Head: to approve on the trip budget and hand the per-diem (refer to the attached table of benefits)."""
    },
    {
        "section": "general_principles",
        "title": "General Principles",
        "content": """• Except for business mandates, collective travel for BU Heads team should be avoided, no more than half of any BU Heads team is allowed to travel on the same flight.
• No more than half of any department should travel together, and managers should keep in mind succession plans when several employees are traveling together.
• A team trip should not exceed 3 people from the same department. More than 3 people travelling together requires the BU Head approval.
• Department Head is responsible for the staff awareness on the implementation of this policy.
• Misrepresenting expenses is considered as a gross misconduct and is grounds for disciplinary action.
• BU Finance Department is authorized to request visibility on all reports related to the trip expenses for controlling purposes."""
    },
    {
        "section": "company_responsibilities",
        "title": "Company Responsibilities & Obligations",
        "content": """Business Travel Arrangements (Accommodation & Airline Tickets):
• The Corporate Travel department is responsible for issuing visas and reserving travel and hotel accommodation for all employees.
• Fees due to changing reservations will be paid by the company after BU Head approval and if the change was according to emergency business needs. Fees paid for any other reason will be borne by the employee.

Travel Expenses:
• Per-diem for all Regions will be paid in US Dollars except for Europe, they will be paid in Euros to the equivalent to USD according to the benefits table attached.
• In case of business trips to attend a training program, the traveler is not entitled for daily per-diem and can claim any training related expenses using the (claim form attached).
• Corporate credit cards with limits of 5,000 to 10,000 USD (to be decided by the BU Finance Head) should be issued to frequent travelers (starting from D3 work level / Directors and above) to avoid advance payments.
• The frequent travelers corporate credit card should be used to cover meals, transportation, and corporate hospitality (please refer to hospitality section) and is also used in case the employee lost his belongings & cash or if an unplanned extension to the trip took place.
• The frequent travelers corporate credit card should not be used for hotel or travel ticket reservations.
• Upon termination of employment for any reason, it is the responsibility of the Line Manager, BU Finance Head and BU HRBP to ensure the following is conducted prior to the employee's exit:
1. Retrieve the corporate card from the employee. Review the card cancellation procedures in the Country addendum and have the card cancelled.
2. Ensure the employee has submitted all expense claims incurred prior to termination.
3. Ensure the corporate card account has been reconciled and all required documentation, including a copy of the final statement is submitted in support of any outstanding balance.
4. Obtain payment from the employee for any amount owed to the Company for non-reimbursable expenses charged to the corporate card, or an approved signed authorization to deduct the same from final pay.
• The company will reimburse the employees for personal property loss necessary for business travel due to fire or natural disaster while traveling or because of the negligence of a common carrier where loss is not covered by the carrier.
• The company will arrange for a proper immunization/vaccination at no cost to the employee when required."""
    },
    {
        "section": "expenses_not_supported",
        "title": "Expenses Not Supported",
        "content": """Expenses not supported by the company:
1. Entertainment expenses.
2. Personal calls.
3. Laundry expenses.
4. Employee personal luggage that exceeds the allowed weight."""
    },
    {
        "section": "employee_responsibilities",
        "title": "Employee Responsibilities & Obligations",
        "content": """Business Communication Tools:
Alternatives to travel such as audio, video or web conference calls should be the first choice considered instead of traveling if:
1. The business location of the collaborating parties of your meeting, presentation or project has teleconferencing capabilities.
2. The event is an internal Company meeting or training session.
3. Teleconferencing is an acceptable alternative with no negative impact on the traveler's business goals.

Business Travel Purpose:
• During the business trip, if the traveler requests an extension for business reasons; the approval of the BU Head is required except for Group Leadership Team members.
• The traveler must submit a written justification for extending the trip to the Line Manager and BU Head.

Travel Business Traveler Responsibilities:
• The company will pay for a full day per diem on the day of departure and the day of arrival; in case the trip starts (flight take-off) at any time before 12:00 noon.
• The company will pay for a half day per diem on the day of departure and the day of arrival; in case the trip starts (flight take-off) at any time after 12:00 noon.
• Any employee entitled for overseas business assignment is responsible for filling out a travel request clarifying the assignment date and purpose approved by Line Manager using Elsewedy Travel Management System.
• Employee must notify the Finance department by at least 5 working days before the travel date to cater for the per-diem and/or advance payment and if a short notice is unavoidable, the BU Finance Head approval should also be acquired."""
    },
    {
        "section": "travel_arrangements",
        "title": "Business Travel Arrangements (Accommodation & Airline Tickets)",
        "content": """• The Traveler should submit his travel request not less than 21 calendar days prior to the date of travel to the Corporate Travel Department for issuing the airline ticket and book accommodation / hotel.
• The Traveler should comply to the visa guidelines available on the Corporate Travel System (EBP)and submit all the required documents on time in full to be able to issue the travel visa.
• For conference rooms or meeting rooms booking for more than 50 people, the traveler should submit his request to the Corporate Travel Department 3 months in advance to guarantee availability and best price.
• Shorter notice requires the BU Head or the BU Finance Head approval.
• Corporate Travel Team shall plan and schedule the business travels enough time prior to the trip, to get the advantage of the most economical rates. When late notification occurs, the Corporate Travel Team shall try to get the best prices possible.
• The cancellation or any changes shall be made immediately or at least 48 hours before the flight date to minimize any extra fees.
• Arrival to the airport must be at least 2 hours before the flight time and any no-show fees imposed because of the employee's late arrival will bear by the employee.
• Travelling with family member is allowed if it has no impact on the business schedule nor added costs on the company. Separate billing is a must.
• In case that the company does not provide accommodation, the company will make an advance payment to the employee according to his work level (refer the table of benefits attached) to help the traveler covering the accommodation expenses.
• Corporate Travel team should book the hotels as per the table of benefits for all travelers unless 5-star hotels are recommended for safety and security reasons in specific regions that are identified in advance by the Corporate Security Department.
• Standard room is the normal accommodation for all employees at all work levels unless upgrades are complimentary by the hotel and with the same rates.
• Airline booking for all employees is according to the (Table of Benefits attached).
• Any trip with flight or flights cost that exceed the amount of USD 2,000 requires the BU Head approval.
• Any upgrade in the hotel and/or the flight class requires the BU Head approval.
• Group Leadership Team members are entitled for business class flights.
• Senior Management (at D1 Grade) are entitled for business class flights only for flights exceeding 4 hours duration. Short flights (4 hours and less) will be booked on economy class for them.
• Travelers suffering from chronic back pain syndrome are entitled for business class flights for flights with duration above 3 hours regardless of their work levels. Such cases should be approved by the Group Medical Director."""
    },
    {
        "section": "transportation",
        "title": "Transportation",
        "content": """Business Need Transportation:
• Transportation includes Taxi, metro, underground, train, and bus.
• It is recommended to use the most convenient, safe but as well economic way of transportation available.
• Transportation from home at the home country to the airport; and back from the airport at the home country to the home actual expenses are covered by the home company (traveler is required to present the invoices to the BU Finance Department by maximum one week from the return date, for settlement purposes).
• The hosting company will provide and cover the transportation from/to the airport and from/to the work location.
• If not, the actual transportation expenses are covered by the home company with a maximum limit of 50 USD / day (traveler is required to present the invoices to the BU Finance Department by maximum one week from the return date, for settlement purposes).
• Transportation by taxis should not be taken for journeys within walking distance (15 mins walking / 2 kilometers).
• In the countries where we have legal entities, a coordination must be done through the traveler main department to provide transportation for the employee to and from the office, factory, or site.
• Transportation by taxis can be used.
• Transportation by Rail is considered as an alternative during any domestic travel & standard class will be the option for less than 2 hours travel. (If possible, tickets should be ordered in advance according to business plan).

Personal Transportation:
• Transportation expenses paid for personal reasons will not be covered by the company. The traveler may use his/her per-diem to cover these expenses.
• The employee is responsible for submitting the actual expenses supported by original relevant documents (along with a copy of the passport and airline tickets for the Overseas Trips) to the Finance department by maximum one week from the return date, for settlement purposes."""
    },
    {
        "section": "international_calls",
        "title": "Business International Calls Allowance",
        "content": """• For business trips only; an amount of 25 USD or its equivalent in local currency is provided to the traveler to purchase a bundle of international / roaming calls and internet connection from his home country telecom provider or the hosting country telecom provider.
• This is subject that the business trip exceeds 2 nights. For 2 nights or less, the traveler should use his business line / mobile allowance for calls and internet connection.
• Employees who have international and roaming bundles covered by the business, are not eligible for the above-mentioned allowance."""
    },
    {
        "section": "hospitality",
        "title": "Hospitality",
        "content": """• Hospitality will be reimbursed only if the below is provided: (claim form attached)
1. Name of attendees & the organization they represent.
2. The purpose of the hospitality and business reason.
3. Location where expenses were incurred.
4. Direct Manager Approval.
5. Itemized receipt has been submitted to BU Finance Department."""
    },
    {
        "section": "policy_compliance",
        "title": "Policy Compliance",
        "content": """Elsewedy Electric Shall conduct regular audits in all its facilities and structures to monitor compliance with this policy. The Group could also perform internal surveys or initiatives to encourage the employees to always report violations of its policies. All concerns related to the policy shall be freely raised and appropriately handled and followed up by the Group.

All Elsewedy Electric staff members are expected to report any case of non-compliance with the policy. The employees should be aware that they have a moral and ethical duty to report such instances and should not fear retaliation. The Group recognizes the importance of confidentiality and will grant anonymity to the complainants who wish so, given that such information does not impede the investigation or resolution of the dispute. There should be no limitation to the filing of complaints, in terms of accessibility to all employees and quantity. The Group will make sure that the employees know where and to whom they can refer for denounces or complaints. Elsewedy Electric ensures that appropriate measures and penalties will be applied in case of non-compliance with this policy."""
    },
    {
        "section": "discipline_remediation",
        "title": "Discipline & Remediation",
        "content": """Violations of this policy shall lead to disciplinary action up to, and including, termination of employment/ partnership. All disciplinary actions shall be undertaken in accordance with the Group's sanctions list and with all applicable local laws and other legal requirements.

The remediation shall be undertaken on a case-by-case basis and in accordance with all applicable local laws and other legal requirements."""
    },
    {
        "section": "policy_review",
        "title": "Policy Review",
        "content": """This policy shall be reviewed annually and/or when deemed necessary."""
    },
    {
        "section": "table_of_benefits",
        "title": "Table of Benefits",
        "content": """Bands | Grades | Professional Level Titles | Class of Flight | Daily Travel Allowance | Accommodation Grade
CEO | | Group CEO | | Actual Expenses | 5 Stars - full board
Leadership | L1 | Group Vice President | Business Class for all Flights | $120 | 4-5 Stars B&B
Leadership | L2 | Sector CEO Group C Level A | Business Class for all Flights | $120 | 4-5 Stars B&B
Leadership | L3 | Managing Director Group C Level B | Business Class for all Flights | $120 | 4-5 Stars B&B
Senior Management | D1 | General Manager Group Director Sector Director | Business Class for Flights > 4 hours | $100 | 4-5 Stars B&B
Senior Management | D2 | Director A | Economy Class | $100 | 4-5 Stars B&B
Senior Management | D3 | Director B | Economy Class | $100 | 4-5 Stars B&B
Management | M1 | Senior Manager | Economy Class | $90 | 3-4 Stars B&B
Management | M2 | Manager A | Economy Class | $90 | 3-4 Stars B&B
Management | M3 | Manager B | Economy Class | $90 | 3-4 Stars B&B
Senior Professionals | S1 A1 | Section Head | Economy Class | $70 | 3-4 Stars B&B
Senior Professionals | S2 | Team Lead | Economy Class | $70 | 3-4 Stars B&B
Professionals | P1 A2 | Senior Engineer Senior Specialist | Economy Class | $70 | 3-4 Stars B&B
Professionals | P2 | Engineer Specialist | Economy Class | $70 | 3-4 Stars B&B
Professionals | P3 A3 | Junior Engineer GDP Specialist Coordinator | Economy Class | $70 | 3-4 Stars B&B
Technicians & Workers | T1 | Supervisor Foreman | Economy Class | $50 | 3-4 Stars B&B
Technicians & Workers | T2 A4 | Senior Technician Driver G1 | Economy Class | $50 | 3-4 Stars B&B
Technicians & Workers | T3 | Technician Driver G2 | Economy Class | $50 | 3-4 Stars B&B
Technicians & Workers | T4 | Assistant Technician | Economy Class | $50 | 3-4 Stars B&B"""
    },
    {
        "section": "hotel_booking_limits",
        "title": "Hotels Booking Limits",
        "content": """Level | Europe | ME, GCC & Africa | USA | Latin America
Leadership | to 450 EUR/GBP | up to 400 $ | up to 400 $ | up to 200 $
Senior Management | up to 300 EUR/GBP | up to 200 $ | up to 250 $ | up to 150 $
Management and Professionals | up to 200 EUR/GBP | up to 180 $ | up to 200 $ | up to 100 $"""
    },
    {
        "section": "version_control",
        "title": "Version Control",
        "content": """Title of Document: Business Trip - Overseas Policy
Version no.: 3
Confidentiality status: To circulate to all employees
Document owner: Group Total Rewards and Organization Design
Document reviewer: Group HR Center of Excellence
Document approver: Group CHRO, Group CFO and Group CEO
Date of creation: 23 November 2022
Version updated date: 16 April 2024
Communication & trainings: By BU HRBPs
Date of next Review: January 2025"""
    }
],

[

    {
        "id": "trm_definition",
        "section": "TRM Definition and Core Concept",
        "content": "The TRM is an annual strategic forum where human resources and business leaders collectively evaluate the future potential of all employees by looking into 2 pillars: the Performance History and Talent Capabilities. Performance History is represented by the employee's achievements versus his/her set goals over the last 2-3 years. Talent Capabilities are represented by the employee's demonstrated level of competencies over the last 2-3 years, the level of education, the depth and breadth of relevant experience, the set of technical skills, cross-functional knowledge, the abilities, personal preferences and values."
    },


    {
        "id": "trm_main_purpose",
        "section": "TRM Main Purpose",
        "content": "The main purpose of the TRM is: To align Talent management efforts with Business Strategy, allowing organizations to build the right capabilities for future challenges."
    },


    {
        "id": "trm_functions",
        "section": "TRM Functions and Services",
        "content": "The TRM serves in: 1- Identifying candidates who can step into key roles or higher grades in the future (nominated High Potentials and Watch-Listers), ensuring leadership continuity and mitigating risks associated with unplanned/ad-hoc vacancies. 2- Facilitating the creation of their Personal Development Plans 'PDPs', aligning individual growth with the organization's needs. 3- Identifying capabilities and skill gaps or shortages in the organization and develop strategies to address them, either through development, hiring, or role changes. 4- Identifying average talent and average performers, allowing the organization to support their improvement through Performance Improvement Plans 'PIPs'. 5- Identifying low performers and consider an exit strategy. 6- The Talent Review decisions are a key input for the merit increase exercise, as merit or base pay decisions are based on the future potential of the talent."
    },


    {
        "id": "merit_increase_timing",
        "section": "Merit Increase Timing",
        "content": "It is worth mentioning that, The ideal scenario is the hold the merit increase exercise post the TAC 'Talent Assessment Centers' for HiPo and Watch-listers confirmation, but due to the tight time between the PA 'Performance Appraisal' exercise scheduled in November and December and the Merit Increase scheduled in January, we use the results of the TRM for the Merit Increase. We offer 2 adjustments cycle in April and October especially to fix the lay of the Confirmed HiPo employees post the TAC."
    },


    {
        "id": "trm_types",
        "section": "TRM Types and Structure",
        "content": "We have 3 types of TRM: Type 1: The Operations Departments TRM - BU level, Sector/Country level (M+SM bands). Type 2: The Commercial Departments TRM - BU level, Sector/Country level (M+SM bands). Type 3: The Support Departments TRM (Finance, HR, IT, and MarCom) - Sector level, Group level. By 'Operations' we mean all the departments except the 'Commercial' and 'Support Departments'. The TRM is done for each Band separately: for Professionals, Senior Professionals, Management and Senior Management. This means that each BU will hold 4 TRMs for the Operations Departments and 4 TRMs for the Commercial Departments."
    },


    {
        "id": "level1_bu_trm_process",
        "section": "Level 1 BU TRM Process",
        "content": "Level 1: The Business Unit TRM - All the business units of Elsewedy Electric Group. 1. The BU HRBP prepares the pre-work sheets and shares them with the BU Heads of Departments. 2. Every Department's Head revises the Performance History of his/her employees and completes the Capabilities Assessment sheet before submitting back to the BU HRBP. 3. The BU HRBP revises the sheets and calls for the BU TRM. 4. The BU HRBP holds the TRM. Attendees: the BU Head, the BU HRBP, the BU Departments' Heads. 5. The BU Head leads the discussion while the BU HRBP facilitates it, takes the minutes of meeting and sets the action plan. 6. Post the BU TRM, the BU HRBP shares the minutes of meeting and the action plan with the BU Head and BU Departments' Heads for confirmation, before submitting the BU TRM documents to the Sector/Country HRBP. 7. The TRM of the Bands: Professional and Senior Professional is signed off at the BU level by the BU Head and BU HRBP."
    },


    {
        "id": "level2_sector_trm_process",
        "section": "Level 2 Sector/Country TRM Process",
        "content": "Level 2: The Sector/Country TRM (M+SM bands) - All the sectors of Elsewedy Electric Group: WCA, Electrical Products, Iskraemeco, Engineering & Construction, Digital Solutions and Infrastructure. All the multisector countries where Elsewedy Electric Group operates: Algeria, East Africa, KSA, and Qatar. The Sector/Country TRM is done only for the Management and Senior Management Bands. This means that each Sector/Country will hold 2 TRMs for the Operations Departments and 2 TRMs for the Commercial Departments. 8. The Sector/Country HRBP and Sector/Country Talent Management & Development (TM&D) Head revise the BUs TRMs sheets received from the BU HRBPs and calls for the Sector/Country TRM. Attendees: The Sector/Country Head, the BUs Heads, the Sector/Country HRBP, the Sector/Country TM&D, the Sectors Departments Heads."
    },


    {
        "id": "support_departments_trm",
        "section": "Support Departments TRM Process",
        "content": "3. The Support Departments TRM. Departments in scope are the Group Support Departments: Finance, Human Resources, Information Technology, and MarCom. The Support Departments TRM is done at the Group and Sector levels. The TRM is done for each Band separately: for Professionals, Senior Professionals, Management and Senior Management. This means that each BU, and Sector/Country will hold 4 TRMs. Level 1: The Sector level - The Sector/Country HRBP and Sector/Country TM&D prepare the pre-work sheets with the Sector/Country Support Departments Heads and shares them with the Group Support Departments HRBP and Group Talent Management Team (TM). Level 2: The Group and Sector level - The Group Support Departments HRBP and Group TM Team consolidate the sheets, revise them and share them as a pre-read with the Group and Sectors' Support Departments Heads."
    },


    {
        "id": "capabilities_scoring_table",
        "section": "Capabilities Attributes Scoring Table",
        "content": "Capabilities Attributes Scoring: 1. Core Behaviours - Performance Appraisal (HRBP input) - Weight: P Band 30%, S Band 20%, M Band 20%, D Band 15%. 2. Leadership Competencies - Performance Appraisal (HRBP input) - Weight: P Band NA, S Band 20%, M Band 30%, D Band 40%. 3. Experience - Records (CV or Talent Profile) versus the Functional Career Path (HRBP and Line Manager input) - Weight: P Band 20%, S Band 20%, M Band 20%, D Band 30%. 4. Education - Records (CV or Talent Profile) (HRBP input) - Weight: P Band 30%, S Band 20%, M Band 10%, D Band NA. 5. Cross-functional knowledge - Informal discussion and observation, or 1-to-1 interview (Line Manager input) - Weight: P Band NA, S Band 10%, M Band 10%, D Band 10%. 6. Technical Skills - Performance Appraisal (technical skills assessment section) (Line Manager input) - Weight: P Band 20%, S Band 10%, M Band 10%, D Band 10%."
    },


    {
        "id": "nine_box_grid_definition",
        "section":" 9-Box Grid Definition",
        "content": "The 9 box grid is a well-known tool for talent management and succession planning in which employees are segmented into 9 groups based on 2 dimensions – Performance and Capabilities. The purpose of this matrix is to closely align talent management and development initiatives to where they add the most value."
    },


    {
        "id": "box1_low_performers",
        "section":" Box 1 - Low Performers",
        "content": "Box 1: Low Performers (LP) - They are the employees who score low on performance and low on capabilities. Our Talent Management and Development efforts should focus on employees with greater potential for growth and contribution rather than on the LP. Action Plan: 1. Identify personal roadblocks that may cause low performance and lack of growth. Seek more suitable roles for these individuals, aligning their skills with the organization's needs and their career growth. However, be careful not to over-invest. 2. If this option is not feasible or doesn't bring quick wins, you should create an exit plan together where you help the person find a role that better suits their skills outside of your organization."
    },


    {
        "id": "box2_4_average_performers",
        "section":" Box 2 and 4 - Average Performers",
        "content": "Box 2: Average Talent (AT) - They are the employees who meet performance expectations / goals and they do a good enough job, but lake many attributes in their talent profile capabilities that are required to deliver properly on their jobs and be (Key Talents ' KT'). Box 4: Average Performers (AP) - They are the employees who have some capabilities to be great, but they are not performing as expected to meet their goals. Here, the question is why they are not performing. Action Plan for Boxes 2 and 4: 1. You may sit with the employee to see if there is a more appropriate assignment where they (and you) can utilize their capabilities better. 2. Up or out plans called Performance Imrpovement Plans (PIP). Create a performance improvement plan by going over personal roadblocks and skills required for the role that the employee needs to work on. 3. Provide measurable expectations and clearly define what good performance will look like. The employee should clearly know what is expected of them. 4. Check in every month and evaluate progress on the plan. Always document these meetings well, as this will help you make a better decision. The employee will also benefit from a structured plan and feedback. 5. If performance does not improve within 6-12 months, you should create an exit plan together where you help the person find a role that better suits their needs outside of your organization."
    },


    {
        "id": "box3_solid_performers",
        "section":" Box 3 - Solid Performers",
        "content": "Box 3: Solid Performers (SP) - They are the employees who score high in performance but low in capabilities. They are the ones who you should take care of in your organization growth. However, they likely don't have much capabilities for career progression. Action plan: 1. Ensure that these employees are rewarded and engaged to make a meaningful contribution. 2. Raise salaries nominally but be careful with substantial raises and bonuses. Do not promote beyond their potential."
    },


    {
        "id": "box5_6_8_key_talent_watchlisters",
        "section":" Box 5, 6, 8 - Key Talent and Watchlisters",
        "content": "Box 5: Key Talent (KT) - They are the employees who are consistent performers and also have the capabilities to grow further in their current roles. Box 8: Watchlisters (WL) - They are the employees who are consistent in showing high capabilities but needs to put extra effort on performance. Box 6: Watchlisters (WL) - They are the employees who are consistent in high performance and over ahcieving their goals but require more development to grow further. Action Plan for boxes 6 and 8: 1. Give employees who are new in their roles the time to develop to the highest level. 2. Expose them to short-term job rotations schemes to expose them to other experiences that will help them perform better or job enlargement by adding activities that fit the employee. 3. Enable them with peer coaching by a HiPo employee or professional coaching to solve any personal or professional issues that hold the person back. In other words, help them overcome performance barriers. 4. Provide these professionals with classroom training and on-the-job learning opportunities that help them develop the skills that they are good at or bring skills that hold them back to a higher level."
    },


    {
        "id": "box7_quality_talent",
        "section":" Box 7 - Quality Talent",
        "content": "Box 7: Quality Talent (QT) - They are the employees who score high in capabilities but low in performance. Action plan: 1. Give these employees time to develop but monitor their performance, they should grow and increase their performance rapidly. You are not only looking for improvements but for stable, solid performance. 2. Communicate that you believe in their potential but also that they should improve their current performance. 3. Communicate clear expectations for their current role so they know what is expected of them. 6. If they still score low in performance a year onward, you should create an exit plan together where you help the person find a role that better suits their needs outside of your organization."
    },


    {
        "id": "box9_high_potentials",
        "section":" Box 9 - High Potentials",
        "content": "Box 9: High Potentials (HiPo) - They are the employees who are referred as future leaders, they are your high performers who are also capable of taking on new roles. These are your A-players and most valuable employees. They also play a critical role in succession management. Action plan: 1. Give your stars challenging assignments. Examples are important internal projects, turnaround projects, or more external opportunities in start-ups or spin-off companies. 2. Check in with them regularly and assess if they are still happy in their current role. Ensure that you spot early signs of dissatisfaction. Praise them and ensure that they feel appreciated for the contributions they make to the company. 3. Provide mentorship with more senior members of the organization. 4. Create networking opportunities with other stars, committees, and with senior members of the organization. These opportunities help to build a network between your top performers and your senior leadership. 5. Reward them and ensure that they receive competitive compensation. These employees contribute the most to your organization, and you should reward them accordingly."
    },


    {
        "id": "trm_technique_flow",
        "section":" TRM Technique and Flow",
        "content": "5. Technique during the Talent Review Meeting. This shirt briefing is intended as an introduction to TRMs and is particularly useful for new TRM members and for the HRBP facilitating these meetings. The exercise is expected to last for around 60 mins discussion for each band. Flow of discussions: 1. Discussion 1: the HiPo and Watch-Listers together (boxes: 9-6-8), 2. Discussion 2: the key Talent, Solid Performers and Quality Talent together (boxes: 5-3-7) 3. Discussion 3: the Low Performers, Average Talent and Average Perfromers together (boxes: 1-2-4). For each of the above 3 discussions, we go through 3 steps: Step 1: look into the 2-3 years performance scores for all the pool of employees in the targeted boxes. Step 2: look into their 2-3 capabilities scores. So you assess each dimension/axis seperately without bias. Step 3: plot performance and capabilities on a 3×3 grid, resulting in the 9-Box Grid."
    },


    {
        "id": "performance_categories",
        "section":" Performance Categories",
        "content": "Performance categories. Mark the relevant box in front of each employee: - Left: employees who do not deliver expected results as consistently as peers - Mid: employees who deliver expected results consistently in comparison to peers - Right: employees who are the very best at delivering outstanding results (consistently overachieving his/her goals versus peers)"
    },


    {
        "id": "capabilities_categories",
        "section":" Capabilities Categories  ",
        "content": "Capabilities categories. Mark the relevant box in front of each employee: - Bottom: employees who do not demonstrate the expected capabilities as consistently as peers - Mid: employees who fully and consistently demonstrate the expected capabilities required for the current band in comparison to peers - Top: employees who are the very best at consistently demonstrating outstanding capabilities qualifying them to move to the higher band"
    },


    {
        "id": "post_trm_guidelines",
        "section":" Post-TRM Guidelines",
        "content": "Post the TRM: Communicating the TRM results to the employees should be done by the Line Manager. It has to be based on objective data. High Potential Employees need to understand that the results of the TRM are inintial and considered as 'nominations' and not final. The (nominated HiPo) are enroleed into a Talent Assessement Center 'TAC' to confirm their nomnations. Similarly, you should also be careful about telling employees they are eligible for a salary adjustments or promotion, or that they are nominated as successors. These decisions take place post the 'TAC'. And as well, there may not be any job openings available at the moment to fulfill this."
    },


    {
        "id": "important_notes",
        "section":" Important Notes",
        "content": "Note: Segmenting and categorizing talent is not about placing people in boxes. Instead, it is about thinking what talent the organization will require in the future and ensuring a ready talent supply through targeted development and other initiatives. An employee's position on the 9-box grid can shift by only one adjacent box from one year to the next, ensuring gradual progression or regression. The Owner of the TRM, is the person who opens up the discussions and manages the flow of questions. This person is the Business Head (BU Head, or Sector/Country Head), or Group Department Head for the Group Support Departments TRMs. The Facilitator of the TRM, is the person who prepares the data, shares the pre-work, calls for the meeting, manages the timing, take the minutes and wrote down the action plan. This person is the HRBP for the BU/Sector/Country supported by the Sector/Country TM&D, or Group TM&D Team for the Group Support Departments TRMs. The Personal Development Plan 'PDP' is a magic retention tool for the Watch-listers and High Potential Talents."
    }
],
]


metas = [
 {
        "policy_name": "Employee Loans Policy",
        "policy_name_ar": "سياسة سلف العاملين",
        "keywords": ["loans", "employee loans", "advance", "guarantors", "سلف", "العاملين", "قروض", "ضمانات"]
    },

 {
        "policy_name": "Employee Loans Policy",
        "policy_name_ar": "سياسة سلف العاملين",
        "keywords": ["loans", "employee loans", "advance", "guarantors", "سلف", "العاملين", "قروض", "ضمانات"]
    },

 {
        "policy_name": "Internal Job Posting Criteria",
        "policy_name_ar": "معايير الإعلان عن الوظائف الداخلية",
        "keywords": ["internal", "job posting", "recruitment", "hiring", "mobility", "career", "promotion", "transfer", "داخلي", "إعلان وظائف", "توظيف", "تعيين", "حراك وظيفي", "مسار مهني", "ترقية", "نقل"]
    },

    {
        "policy_name": "Internal Mobility Policy",
        "policy_name_ar": "سياسة التنقل الداخلي",
        "keywords": ["mobility", "transfer", "internal", "job posting", "lateral", "vertical", "promotion", "career development", "تنقل", "نقل", "داخلي", "وظائف", "ترقية", "تطوير مهني"]
    },

    {
        "policy_name": "End of Year Performance Appraisal Exercise 2024",
        "policy_name_ar": "تقييم الأداء نهاية العام 2024",
        "keywords": ["performance", "appraisal", "evaluation", "goals", "competencies", "bell curve", "rating", "business goals", "behaviors", "تقييم", "أداء", "أهداف"]
    },

    {
    "policy_name": "Learning & Development Policy",
    "policy_name_ar": "سياسة التعلم والتطوير",
    "keywords": ["learning", "development", "training", "education", "skills", "competencies", "academies", "programs", "leadership", "talent", "التعلم", "التطوير", "التدريب", "التعليم", "المهارات", "الكفاءات", "الأكاديميات", "البرامج", "القيادة", "المواهب"]
    },

    {
    "policy_name": "Talent Differentiation and Merit Increase Exercise 2024",
    "policy_name_ar": "تمرين تمييز المواهب وزيادة الاستحقاق 2024",
    "keywords": ["talent", "merit", "performance", "appraisal", "bonus", "differentiation", "9-box grid", "25-box grid", "مواهب", "استحقاق", "أداء", "تقييم", "مكافأة", "تمييز"]
    },

    {
    "policy_name": "Dress Code & Personal Appearance Policy",
    "policy_name_ar": "سياسة قواعد اللباس والمظهر الشخصي",
    "keywords": ["dress code", "appearance", "uniform", "professional attire", "workplace standards", "لباس", "مظهر", "زي موحد", "مهني", "معايير العمل"]
  },

  {
        "policy_name": "Car Allowance Policy - Egypt Industrial Zones",
        "policy_name_ar": "سياسة بدل السيارة - المناطق الصناعية المصرية",
        "keywords": ["car allowance", "vehicle allowance", "factory", "management", "بدل سيارة", "مصانع", "إدارة", "سيارات"]
    },

    {
        "policy_name": "Manpower Planning Exercise 2025",
        "policy_name_ar": "تمرين تخطيط القوى العاملة 2025",
        "keywords": ["manpower", "planning", "hiring", "recruitment", "personnel", "budget", "headcount", "GDP", "early talent", "قوى عاملة", "تخطيط", "توظيف", "استقطاب", "موظفين", "ميزانية"]
    },

    {
        "policy_name": "Global Mobility Policy",
        "policy_name_ar": "سياسة التنقل العالمي",
        "keywords": ["mobility", "global", "international", "assignment", "transfer", "relocation", "STA", "LTA", "localization", "expatriate", "تنقل", "عالمي", "انتداب", "نقل"]
    },

    {
        "policy_name": "Exceptional Loan Policy",
        "policy_name_ar": "سياسة سلف العاملين الاستثنائية",
        "keywords": ["loan", "exceptional", "employee", "marriage", "disasters", "hajj", "emergency", "سلف", "استثنائية", "عاملين", "زواج", "كوارث", "حج"]
    },

    {
        "policy_name": "Exceptional Loan Policy",
        "policy_name_ar": "سياسة سلف العاملين الاستثنائية",
        "keywords": ["loan", "exceptional", "employee", "marriage", "disasters", "hajj", "emergency", "سلف", "استثنائية", "عاملين", "زواج", "كوارث", "حج"]
    },

    {
        "policy_name": "Promotion Policy",
        "policy_name_ar": "سياسة الترقية",
        "keywords": ["promotion", "career advancement", "talent management", "9-box grid", "HIPO", "high potential", "watch-lister", "key talent", "TAC", "talent assessment", "band promotion", "grade promotion", "ترقية", "تطوير مهني", "إدارة المواهب", "تقييم المواهب"],
        "related_processes": "Talent Review Meeting, Talent Assessment Center, Performance Management"
    },

    {
    "policy_name": "Salary Adjustment Exercise Policy",
    "policy_name_ar": "سياسة تعديل الراتب",
    "keywords": ["salary", "adjustment", "compensation", "9-box grid", "talent differentiation", "HIPO", "watch-listers", "comp-ratio", "راتب", "تعديل", "تعويض", "مواهب", "أداء"],
  },

  {
        "policy_name": "Standard Recruitment Process on Taleo",
        "policy_name_ar": "عملية التوظيف المعيارية على نظام تاليو",
        "keywords": ["recruitment", "hiring", "Taleo", "job requisition", "candidate selection", "توظيف", "استقطاب", "طلب وظيفة", "اختيار المرشحين", "تاليو"]
    },

    {
        "policy_name": "Group Transportation Policy",
        "policy_name_ar": "سياسة النقل الجماعي",
        "keywords": ["transportation", "allowance", "buses", "pool cars", "commute", "نقل", "مواصلات", "بدل", "حافلات"]
    },

    {
        "policy_name": "Business Trip Overseas Travel Policy",
        "policy_name_ar": "سياسة السفر للخارج للأعمال",
        "keywords": ["travel", "overseas", "international", "business trip", "accommodation", "flight", "per-diem", "expenses", "corporate credit card", "سفر", "خارج", "دولي", "رحلة عمل", "إقامة", "طيران", "مصروفات"],
    },

    {
        "policy_name": "Talent Review Meeting and 9-Box Grid of Talent Differentiation",
        "policy_name_ar": "اجتماع مراجعة المواهب وشبكة التسع مربعات لتمييز المواهب",
        "keywords": ["talent management", "performance review", "9-box grid", "high potential", "succession planning", "capability assessment", "إدارة المواهب", "مراجعة الأداء", "شبكة التسع مربعات", "إمكانات عالية", "تخطيط الخلافة", "تقييم القدرات"]
    },


]