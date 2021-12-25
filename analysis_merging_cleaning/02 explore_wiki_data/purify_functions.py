from all_funcs import *
master_mapping=[
    {
        "attr_name": "pageid",
        "freq": 3469,
        "sample": 4210106,
        "parent_attr": "wikipedia_page_id",
        "func": None
    },
    {
        "attr_name": "url",
        "freq": 3469,
        "sample": "https://en.wikipedia.org/wiki/Abraham_Silberschatz",
        "parent_attr": "wikipedia_page_url",
        "func": None
    },
    {
        "attr_name": "title",
        "freq": 3469,
        "sample": "Abraham_Silberschatz",
        "parent_attr": "person_name",
        "func": None
    },
    {
        "attr_name": "backlinks",
        "freq": 3469,
        "sample": [
            "Database",
            "Windows 2000",
            "Process (computing)",
            "Program counter",
            "Memory management",
            "Scheduling (computing)",
            "Round-robin scheduling",
            "Two-phase locking",
            "Join (SQL)",
            "Page table",
            "Slab allocation",
            "Multivalued dependency",
            "List of Stony Brook University people",
            "Global serializability",
            "Kernel (operating system)",
            "C. Mohan",
            "Talk:Abraham Silberschatz",
            "User:Tony Sidaway/Living people/tranche 082",
            "User:Dingo1729/History of commitment ordering",
            "Database System Concepts",
            "User:Ibon.coria/sandbox",
            "Wikipedia:Administrators' noticeboard/IncidentArchive822",
            "User:Rebone System/sandbox",
            "User:H@r@ld/opensyllabus",
            "List of fellows of the Association for Computing Machinery",
            "User talk:Tom29739/Archive 27",
            "User:Oshwah/TalkPageArchives/2017-06",
            "User talk:Tom29739/Archive 30",
            "User talk:Tom29739/Archive 32",
            "User talk:Tom29739/Archive 34",
            "User talk:Tom29739/Archive 36",
            "User talk:Tom29739/Archive 38",
            "User talk:Tom29739/Archive 39",
            "User talk:Tom29739/Archive 43",
            "User talk:Tom29739/Archive 45",
            "File:Database System Concepts.jpg"
        ],
        "parent_attr": "backlinks_to_other_wiki_pages",
        "func": purify_backlinks
    },
    {
        "attr_name": "categories",
        "freq": 3469,
        "sample": [
            "Category:American computer scientists",
            "Category:American computer specialist stubs",
            "Category:Fellow Members of the IEEE",
            "Category:Fellows of the Association for Computing Machinery",
            "Category:Living people",
            "Category:Stony Brook University alumni",
            "Category:Yale University faculty"
        ],
        "parent_attr": "wikipedia_categories_associated_with",
        "func": purify_categories
    },
    {
        "attr_name": "ire_person_name",
        "freq": 3469,
        "sample": "Abraham Silberschatz",
        "parent_attr": "ire_person_name",
        "func": None
    },
    {
        "attr_name": "ire_wiki_id",
        "freq": 3469,
        "sample": 0,
        "parent_attr": "",
        "func": None
    },
    {
        "attr_name": "links",
        "freq": 3468,
        "sample": [
            "ACM Fellow",
            "Bell Labs",
            "C. Mohan",
            "Computer Science",
            "Computer scientist",
            "Database System Concepts",
            "Database systems",
            "Doctoral advisor",
            "Google Scholar",
            "Haifa, Israel",
            "ISNI (identifier)",
            "Operating systems",
            "RERO (identifier)",
            "Raghu Ramakrishnan",
            "Research",
            "SUDOC (identifier)",
            "State University of New York",
            "Stony Brook University",
            "University of texas at austin",
            "VIAF (identifier)",
            "Yale University"
        ],
        "parent_attr": "wiki_pages_accessible_from_person_wiki_page",
        "func": None
    },
    {
        "attr_name": "label",
        "freq": 3468,
        "sample": "Abraham Silberschatz",
        "parent_attr": "person_name",
        "func": None
    },
    {
        "attr_name": "sex or gender (P21)",
        "freq": 3425,
        "sample": "male (Q6581097)",
        "parent_attr": "person_gender",
        "func": purify_gender
    },
    {
        "attr_name": "occupation (P106)",
        "freq": 3354,
        "sample": [
            "computer scientist (Q82594)",
            "engineer (Q81096)"
        ],
        "parent_attr": "person_job",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "given name (P735)",
        "freq": 2890,
        "sample": "Abraham (Q17997608)",
        "parent_attr": "person_name",
        "func": rem_wikidata_page_id
    },
    {
        "attr_name": "educated at (P69)",
        "freq": 2880,
        "sample": [
            "Stony Brook University (Q969850)",
            "State University of New York (Q1140241)",
            "IDF Junior Command Preparatory Boarding School (Q7063325)"
        ],
        "parent_attr": "institutions_educated_in",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "date of birth (P569)",
        "freq": 2625,
        "sample": "+1947-05-01T00:00:00Z",
        "parent_attr": "person_dob",
        "func": purify_date_of_birth
    },
    {
        "attr_name": "Freebase ID (P646)",
        "freq": 2484,
        "sample": "/m/0bq3td",
        "parent_attr": "",
        "func": None
    },
    {
        "attr_name": "employer (P108)",
        "freq": 2461,
        "sample": "Yale University (Q49112)",
        "parent_attr": "employer_orgs",
        "func": rem_wikidata_page_id
    },
    {
        "attr_name": "country of citizenship (P27)",
        "freq": 2456,
        "sample": "United States of America (Q30)",
        "parent_attr": "country_of_citizenship",
        "func": rem_wikidata_page_id
    },
    {
        "attr_name": "name",
        "freq": 2283,
        "sample": "Avi Silberschatz",
        "parent_attr": "person_name",
        "func": None
    },
    {
        "attr_name": "redirects",
        "freq": 2104,
        "sample": [
            {
                "pageid": 5101640,
                "ns": 0,
                "title": "Elizabeth Holberton"
            },
            {
                "pageid": 17840780,
                "ns": 0,
                "title": "Frances Elizabeth Snyder"
            },
            {
                "pageid": 26730142,
                "ns": 0,
                "title": "Frances Elizabeth Holberton"
            },
            {
                "pageid": 47787329,
                "ns": 0,
                "title": "Betty Snyder"
            }
        ],
        "parent_attr": "person_name",
        "func": None
    },
    {
        "attr_name": "WorldCat Identities ID (P7859)",
        "freq": 1998,
        "sample": "lccn-n82162524",
        "parent_attr": "",
        "func": None
    },
    {
        "attr_name": "Library of Congress authority ID (P244)",
        "freq": 1878,
        "sample": "n82162524",
        "parent_attr": "",
        "func": None
    },
    {
        "attr_name": "family name (P734)",
        "freq": 1833,
        "sample": "Holberton (Q37565704)",
        "parent_attr": "person_name",
        "func": rem_wikidata_page_id
    },
    {
        "attr_name": "description",
        "freq": 1809,
        "sample": "American computer programmer",
        "parent_attr": "",
        "func": None
    },
    {
        "attr_name": "alma_mater",
        "freq": 1805,
        "sample": "[[Stony Brook University]]<br />[[Yale University]]",
        "parent_attr":"institutions_educated_in",
        "func": get_univs_from_alma_mater
    },
    {
        "attr_name": "place of birth (P19)",
        "freq": 1660,
        "sample": "Haifa (Q41621)",
        "parent_attr": "place_of_birth",
        "func": rem_wikidata_page_id
    },
    {
        "attr_name": "award received (P166)",
        "freq": 1628,
        "sample": [
            "ACM Fellow (Q18748039)",
            "IEEE Fellow (Q111734)"
        ],
        "parent_attr": "awards_received",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "birth_date",
        "freq": 1570,
        "sample": "{{Birth date|1917|3|7}}",
        "parent_attr": "person_dob",
        "func": purify_birth_date
    },
    {
        "attr_name": "aliases",
        "freq": 1565,
        "sample": [
            "Avi Silberschatz"
        ],
        "parent_attr": "person_name",
        "func": None
    },
    {
        "attr_name": "doctoral advisor (P184)",
        "freq": 1515,
        "sample": [
            "Arthur Jay Bernstein (Q102077480)",
            "Richard Kieburtz (Q68622015)"
        ],
        "parent_attr": "doctoral advisor(s)",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "Mathematics Genealogy Project ID (P549)",
        "freq": 1432,
        "sample": "94554",
        "parent_attr": "",
        "func": None
    },
    {
        "attr_name": "birth_place",
        "freq": 1411,
        "sample": "[[Philadelphia, Pennsylvania]]",
        "parent_attr": "person_birth_place",
        "func": purify_birth_place
    },
    {
        "attr_name": "image",
        "freq": 1407,
        "sample": "Avi silberschatz.jpg",
        "parent_attr": "person_image_links",
        "func": purify_profile_image
    },
    {
        "attr_name": "known_for",
        "freq": 1324,
        "sample": "[[database systems]]<br>[[operating systems]]",
        "parent_attr": "person_domains",
        "func": purify_known_for
    },
    {
        "attr_name": "doctoral student (P185)",
        "freq": 1177,
        "sample": [
            "C. Mohan (Q5006716)",
            "Raghu Ramakrishnan (Q7282986)",
            "Rajeev Rastogi (Q15995420)",
            "Donald Spencer Fussell (Q102129368)",
            "Iyer Venkateshwaran Ramakrishnan (Q102157550)",
            "Sharad Mehrotra (Q102196909)",
            "Samuel Lycurgus Grier, Jr. (Q102300750)",
            "Sumit Ganguly (Q102300751)",
            "Ernest Samuel Cohen (Q102300752)",
            "Khien Mien Chew (Q102300753)",
            "Banu Rahime Ozden (Q102300754)",
            "Robert Lee Read (Q102300755)"
        ],
        "parent_attr": "person_doctoral_students",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "doctoral_advisor",
        "freq": 1104,
        "sample": "Arthur Bernstein<br>Richard Kieburtz",
        "parent_attr": "doctoral advisor(s)",
        "func": purify_split_by_comma
    },
    {
        "attr_name": "nationality",
        "freq": 1056,
        "sample": "[[United States|American]]",
        "parent_attr": "person_nationality",
        "func": purify_nationality
    },
    {
        "attr_name": "languages spoken, written or signed (P1412)",
        "freq": 996,
        "sample": "English (Q1860)",
        "parent_attr": "languages spoken, written or signed",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "field of work (P101)",
        "freq": 996,
        "sample": "software engineering (Q80993)",
        "parent_attr": "person_domains",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "workplaces",
        "freq": 985,
        "sample": "[[SRI International]] [[Artificial Intelligence Center]]",
        "parent_attr": "person_workplaces",
        "func": purify_workplaces
    },
    {
        "attr_name": "Google Scholar author ID (P1960)",
        "freq": 929,
        "sample": "XF6Yk98AAAAJ",
        "parent_attr": "",
        "func": None
    },
    {
        "attr_name": "member of (P463)",
        "freq": 914,
        "sample": "Institute of Electrical and Electronics Engineers (Q131566)",
        "parent_attr": "",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "fields",
        "freq": 827,
        "sample": "[[Computer Science]]",
        "parent_attr": "person_domains",
        "func": purify_split_by_comma
    },
    {
        "attr_name": "website",
        "freq": 779,
        "sample": "http://www.cs.yale.edu/~avi/",
        "parent_attr": "associated_website",
        "func": None
    },
    {
        "attr_name": "official website (P856)",
        "freq": 760,
        "sample": "http://www.cs.yale.edu/~avi/",
        "parent_attr": "associated_website",
        "func": None
    },
    {
        "attr_name": "field",
        "freq": 744,
        "sample": "[[Computer Science]]",
        "parent_attr": "person_domains",
        "func": purify_split_by_comma
    },
    {
        "attr_name": "thesis_title",
        "freq": 703,
        "sample": "Improving the Accuracy of Computed Matrix Eigenvalues",
        "parent_attr": "person_thesis",
        "func": None
    },
    {
        "attr_name": "awards",
        "freq": 689,
        "sample": "[https://www.witi.com/halloffame/298369/ENIAC-Programmers-Kathleen-/ Women in Technology International Hall of Fame]",
        "parent_attr": "awards_received",
        "func": purify_known_for
    },
    {
        "attr_name": "thesis_year",
        "freq": 671,
        "sample": "1980",
        "parent_attr": "",
        "func": None
    },
    {
        "attr_name": "iwlinks",
        "freq": 563,
        "sample": [
            "https://commons.wikimedia.org/wiki/Per_Brinch_Hansen",
            "https://de.wikipedia.org/wiki/J%C3%B8rgen_Brinch_Hansen"
        ],
        "parent_attr": "",
        "func": None
    },
    {
        "attr_name": "date of death (P570)",
        "freq": 543,
        "sample": "+2001-12-08T00:00:00Z",
        "parent_attr": "person_date_of_death",
        "func": purify_date_of_birth
    },
    {
        "attr_name": "work_institution",
        "freq": 470,
        "sample": "[[Yale University]]",
        "parent_attr": "employer_orgs",
        "func": purify_known_for
    },
    {
        "attr_name": "thesis_url",
        "freq": 429,
        "sample": "http://search.proquest.com/docview/303029334",
        "parent_attr": "",
        "func": None
    },
    {
        "attr_name": "occupation",
        "freq": 418,
        "sample": "[[Computer Scientist]]",
        "parent_attr": "person_job",
        "func": purify_known_for
    },
    {
        "attr_name": "birth_name",
        "freq": 410,
        "sample": "Frances Elizabeth Snyder",
        "parent_attr": "person_name",
        "func": None
    },
    {
        "attr_name": "death_date",
        "freq": 388,
        "sample": "{{Death date and age|2001|12|8|1917|3|7}}",
        "parent_attr": "person_date_of_death",
        "func": purify_birth_date
    },
    {
        "attr_name": "residence (P551)",
        "freq": 386,
        "sample": "Seattle (Q5083)",
        "parent_attr": "person_residence",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "residence",
        "freq": 375,
        "sample": "[[United States]]",
        "parent_attr": "person_residence",
        "func": purify_known_for
    },
    {
        "attr_name": "citizenship",
        "freq": 373,
        "sample": "[[Canada]]",
        "parent_attr": "country_of_citizenship",
        "func": purify_known_for
    },
    {
        "attr_name": "place of death (P20)",
        "freq": 355,
        "sample": "Rockville (Q327022)",
        "parent_attr": "person_death_place",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "doctoral_students",
        "freq": 340,
        "sample": "[[C. Mohan]]<br>[[Raghu Ramakrishnan]]",
        "parent_attr": "person_doctoral_students",
        "func": purify_known_for
    },
    {
        "attr_name": "name in native language (P1559)",
        "freq": 335,
        "sample": "Alexander von Humboldt",
        "parent_attr": "person_name",
        "func": None
    },
    {
        "attr_name": "education",
        "freq": 318,
        "sample": "[[University of Pennsylvania]]",
        "parent_attr": "institutions_educated_in",
        "func": purify_known_for
    },
    {
        "attr_name": "prizes",
        "freq": 310,
        "sample": "ACM Fellow<br>IEEE Fellow<br>AAAS Fellow<br>IEEE Taylor L. Booth Education Award (2002)<br>ACM Karl V. Karlstrom Outstanding Educator Award (1998)<br>ACM SIGMOD Contribution Award (1997)<br> 2019 VLDB Test of Time Award",
        "parent_attr": "awards_received",
        "func": purify_known_for
    },
    {
        "attr_name": "spouse",
        "freq": 299,
        "sample": "John Vaughan Holberton",
        "parent_attr": "person_spouse(s)",
        "func": purify_known_for
    },
    {
        "attr_name": "death_place",
        "freq": 286,
        "sample": "[[Rockville, Maryland]]",
        "parent_attr": "person_place_of_death",
        "func": purify_birth_place
    },
    {
        "attr_name": "notable work (P800)",
        "freq": 262,
        "sample": "ENIAC (Q169399)",
        "parent_attr": "person_notable_work",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "Twitter username (P2002)",
        "freq": 259,
        "sample": "etzioni",
        "parent_attr": "",
        "func": None
    },
    {
        "attr_name": "work_institutions",
        "freq": 204,
        "sample": "[[Stony Brook University]] (2002\u2013present)",
        "parent_attr": "employer_orgs",
        "func": purify_known_for
    },
    {
        "attr_name": "academic degree (P512)",
        "freq": 178,
        "sample": "Doctor of Philosophy (Q752297)",
        "parent_attr": "",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "children",
        "freq": 167,
        "sample": "Priscilla Holberton<br />Pamela Holberton",
        "parent_attr": "person_children",
        "func": purify_known_for
    },
    {
        "attr_name": "work location (P937)",
        "freq": 138,
        "sample": "New York City (Q60)",
        "parent_attr": "",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "spouse (P26)",
        "freq": 128,
        "sample": "novalue",
        "parent_attr": "person_spouse(s)",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "cause of death (P509)",
        "freq": 117,
        "sample": "disease (Q12136)",
        "parent_attr": "person_death_causes",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "Semantic Scholar author ID (P4012)",
        "freq": 117,
        "sample": "143898851",
        "parent_attr": "",
        "func": None
    },
    {
        "attr_name": "LinkedIn personal profile ID (P6634)",
        "freq": 114,
        "sample": "stephenwolfram",
        "parent_attr": "",
        "func": None
    },
    {
        "attr_name": "employer",
        "freq": 102,
        "sample": "[[Moore School of Engineering]]<br /> [[University of Pennsylvania]]  <br/> [[Remington Rand]]<br /> [[National Bureau of Standards]]<br>[[David Taylor Model Basin]]",
        "parent_attr": "employer_orgs",
        "func": purify_known_for
    },
    {
        "attr_name": "manner of death (P1196)",
        "freq": 101,
        "sample": "natural causes (Q3739104)",
        "parent_attr": "person_death_causes",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "position held (P39)",
        "freq": 98,
        "sample": "Geheimrat (Q11165895)",
        "parent_attr": "",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "birth name (P1477)",
        "freq": 91,
        "sample": "Stephen Cole Kleene",
        "parent_attr": "person_name",
        "func": None
    },
    {
        "attr_name": "influences",
        "freq": 87,
        "sample": "{{Plainlist|\n* [[Peter Naur]]\n* [[Edsger W. Dijkstra|Edsger Dijkstra]]\n* [[Niklaus Wirth]]\n* [[Tony Hoare]]\n* [[Ole-Johan Dahl]]}}",
        "parent_attr": "person_has_influenced",
        "func": purify_known_for
    },
    {
        "attr_name": "student (P802)",
        "freq": 84,
        "sample": "Kenneth Seals-Nutt (Q47487399)",
        "parent_attr": "person_doctoral_students",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "father (P22)",
        "freq": 73,
        "sample": "J\u00f8rgen Brinch Hansen (Q1110920)",
        "parent_attr": "person_parents",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "influenced by (P737)",
        "freq": 73,
        "sample": "Friedrich Wilhelm Joseph Schelling (Q60070)",
        "parent_attr": "person_influenced_by",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "native language (P103)",
        "freq": 72,
        "sample": "English (Q1860)",
        "parent_attr": "languages spoken, written or signed",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "religion (P140)",
        "freq": 64,
        "sample": "Lutheranism (Q75809)",
        "parent_attr": "",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "academic_advisors",
        "freq": 63,
        "sample": "[[Markus Herz]], [[Carl Ludwig Willdenow]], [[Abraham Gottlob Werner]]",
        "parent_attr": "doctoral advisor(s)",
        "func": purify_known_for
    },
    {
        "attr_name": "participant in (P1344)",
        "freq": 62,
        "sample": "CODASYL (Q1023961)",
        "parent_attr": "",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "ethnic group (P172)",
        "freq": 52,
        "sample": "Germans (Q42884)",
        "parent_attr": "",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "part of (P361)",
        "freq": 52,
        "sample": "Stanford University Management Science & Engineering Department (Q77247020)",
        "parent_attr": "",
        "func": None
    },
    {
        "attr_name": "notable_students",
        "freq": 50,
        "sample": "[[Louis Agassiz]] {{sfn|Rupke|2008|p|=|54}}",
        "parent_attr": "person_doctoral_students",
        "func": purify_notable_students
    },
    {
        "attr_name": "other_names",
        "freq": 47,
        "sample": "saurik",
        "parent_attr": "person_name",
        "func": None
    },
    {
        "attr_name": "academic thesis (P1026)",
        "freq": 47,
        "sample": "Correctness and communication in real-time systems (Q28911326)",
        "parent_attr": "person_thesis",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "student of (P1066)",
        "freq": 46,
        "sample": "Peter Naur (Q92618)",
        "parent_attr": "doctoral advisor(s)",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "sibling (P3373)",
        "freq": 45,
        "sample": "Wilhelm von Humboldt (Q77888)",
        "parent_attr": "",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "child (P40)",
        "freq": 45,
        "sample": "Jakob Uszkoreit (Q98891246)",
        "parent_attr": "person_children",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "native_name",
        "freq": 45,
        "sample": "\u05e0\u05e4\u05ea\u05dc\u05d9 \u05ea\u05e9\u05d1\u05d9",
        "parent_attr": "person_name",
        "func": None
    },
    {
        "attr_name": "discipline",
        "freq": 42,
        "sample": "Electrical and Computer Engineering",
        "parent_attr": "person_domains",
        "func": purify_known_for
    },
    {
        "attr_name": "affiliation (P1416)",
        "freq": 42,
        "sample": "University of California, Davis, Department of Computer Science (Q104889160)",
        "parent_attr": "",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "influenced",
        "freq": 41,
        "sample": "[[Charles Darwin|Darwin]], [[Alfred Russel Wallace|Wallace]], [[Henry David Thoreau|Thoreau]], [[Walt Whitman|Whitman]], [[Ralph Waldo Emerson|Emerson]], [[John Muir|Muir]], [[Washington Irving|Irving]], [[Ida Laura Pfeiffer]]",
        "parent_attr": "person_influenced_by",
        "func": purify_known_for
    },
    {
        "attr_name": "GitHub username (P2037)",
        "freq": 41,
        "sample": "hmason",
        "parent_attr": "",
        "func": None
    },
    {
        "attr_name": "Fellow of the Royal Society ID (P2070)",
        "freq": 41,
        "sample": "geoffrey-hinton-11624",
        "parent_attr": "",
        "func": None
    },
    {
        "attr_name": "mother (P25)",
        "freq": 38,
        "sample": "Marie-Elisabeth von Humboldt (Q1618375)",
          "parent_attr": "person_parents",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "described at URL (P973)",
        "freq": 38,
        "sample": "http://humboldt.staatsbibliothek-berlin.de/leben/",
        "parent_attr": "associated_website",
        "func": None
    },
    {
        "attr_name": "years_active",
        "freq": 38,
        "sample": "2013\u2013present",
        "parent_attr": "",
        "func": None
    },
    {
        "attr_name": "place of burial (P119)",
        "freq": 37,
        "sample": "Ivy (Q5923360)",
        "parent_attr": "",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "writing language (P6886)",
        "freq": 37,
        "sample": [
            "French (Q150)",
            "German (Q188)"
        ],
        "parent_attr": "languages spoken, written or signed",
        "func": list_rem_wikidata_page_id
    },
    {
        "attr_name": "notable_works",
        "freq": 28,
        "sample": "''The Cyberpunk Handbook'' (1995), ''How to Mutate and Take Over the World'' (1996)",
        "parent_attr": "person_notable_work",
        "func": purify_known_for
    },
    {
        "attr_name": "sub_discipline",
        "freq": 23,
        "sample": "[[Computational complexity theory]]",
        "parent_attr": "person_domains",
        "func": purify_known_for
    },
    {
        "attr_name": "number of children (P1971)",
        "freq": 21,
        "sample": {
            "amount": "+4",
            "unit": "1"
        },
        "parent_attr": "",
        "func": None
    },
    {
        "attr_name": "office",
        "freq": 21,
        "sample": "President of the University of Rochester",
        "parent_attr": "",
        "func": None
    },
    {
        "attr_name": "official blog (P1581)",
        "freq": 20,
        "sample": [
            "http://blog.prof.so/",
            "http://blog.softeng.info/"
        ],
        "parent_attr": "",
        "func": None
    },
    {
        "attr_name": "parents",
        "freq": 20,
        "sample": "John Steele Sproull<BR>Chloe Velma Lamb",
        "parent_attr": "person_parents",
        "func": purify_known_for
    },
    {
        "attr_name": "main_interests",
        "freq": 17,
        "sample": "Philosophy of technology, Ethics and technology, Ethics and information technology, Robot ethics, Environmental philosophy",
        "parent_attr": "person_domains",
        "func": purify_split_by_comma
    },
    {
        "attr_name": "doctoral_advisors",
        "freq": 15,
        "sample": "[[Eric Reissner]]",
        "parent_attr": "doctoral advisor(s)",
        "func": purify_known_for
    },
    {
        "attr_name": "organization",
        "freq": 15,
        "sample": "CognitionX",
        "parent_attr": "",
        "func": None
    },
    {
        "attr_name": "known for",
        "freq": 15,
        "sample": "[[Women's rights|women's rights advocate]]<br />[[National Organization for Women]] (NOW)",
        "parent_attr": "person_domains",
        "func": purify_known_for
    },
    {
        "attr_name": "has works in the collection (P6379)",
        "freq": 14,
        "sample": "Vanderbilt University Fine Arts Gallery (Q18563658)",
        "parent_attr": "",
        "func": None
    },
    {
        "attr_name": "medical condition (P1050)",
        "freq": 14,
        "sample": "prostate cancer (Q181257)",
        "parent_attr": "",
        "func": None
    }
]