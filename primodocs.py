from os import environ
from dotenv import load_dotenv 

load_dotenv()

PRIMO_DOCS = f"""BASE URL: https://api-ap.hosted.exlibrisgroup.com/primo/v1/search

API Documentation
The API endpoint /primo/v1/search accepts . All URL parameters are listed below:

Parameter	Format	Required	Default	    Description
vid	        String	Yes		    N/A         The view ID, always set to "65SMU_INST%3ASMU_NUI" for the call to work
tab	        String 	Yes		    N/A         The name of the tab, always set to "Everything" for the call to work
scope	    String 	Yes         N/A         The scope name, always set to "Everything" for the call to work
q	        String	Yes     	N/A         The query string that you want to use to perform a search.
                                            The query string uses the following format:
                                            q=<field_1>,<precision_1>,<value_1>[[,<operator_1>];<field_n>,<precision_n>,<value_n>...]
                                            * field - The data field that you want to search within. The following fields are valid: any (for any field), title, creator (for author), sub (for subject), and usertag (for tag).
                                            * precision - The precision operation that you want to apply to the field. The following precision operators are valid: exact (value must match the data in the field exactly), begins_with (the value must be found at the beginning of the field), and contains (the value must be found anywhere in the field).
                                            * value - The search terms, which can be a word, phrase, or exact phrase (group of words enclosed by quotes), and can include the following logical operators: AND, OR, and NOT. For more information regarding search terms, see https://knowledge.exlibrisgroup.com/Primo/Product_Documentation/New_Primo_User_Interface/End_User_Help/010Performing_Basic_Searches.
                                            * operator - When specifying multiple search fields for advanced searches, this parameter applies the following logical operations between fields: AND (specified values must be found in both fields), OR (specified values must be found in at least one of the fields), NOT (the specified value of the next field must not be found). If no operator is specified, the system defaults to AND.

                                            Note: Multiple fields are delimited by a semicolon.
                                            Limitation: The value must not include a semicolon character.

                                            In the following example, the system searches for all records in which the word home is found anywhere within the record's title:
                                            q=title,contains,home

                                            In the following example, the system searches for all records in which the title field contains the words pop and music and the subject field contains the word korean:
                                            q=title,contains,pop music,AND;sub,contains,korean
inst	    String	Yes     	N/A         The Institution code. Always set to "65SMU_INST" for the call to work
apiKey      String  Yes         N/A         Use the API key here {environ.get("PRIMO_API_KEY")}
offset      Int     No          0           The offset of the results from which to start displaying the results. For first request, set to 0 first
limit       Int     No          5           The maximum number of results in the response. Set this limit to 5 when requesting

For more information regarding other fields of the API, refer to https://developers.exlibrisgroup.com/primo/apis/docs/primoSearch/R0VUIC9wcmltby92MS9zZWFyY2g=/
If the response doesn't require additional resources or has no queries, return the received request as response
"""