jindal_vivek10@cloudshell:~/projects (vjindal-project-ai-basic)$ **git clone https://github.com/jindalvivek10/fastmcp-simple-adk.git fastmcp-simple-adk**             

jindal_vivek10@cloudshell:~/projects/fastmcp-simple-adk/fastmcp-simple/fastmcp_simple$ **uv run python server.py**
(run the server locally)

In a new terminal, run the client and in reality we are able to see the results of the files present in the DEsktop folder, just by running the below command.. 

jindal_vivek10@cloudshell:~/projects/fastmcp-simple-adk/fastmcp-simple$**uv run python fastmcp_simple/client.py**

Open the git repository and then make changes to the files and stage, commit and then sync the changes to your project ..

jindal_vivek10@cloudshell:~/projects/fastmcp-simple-adk/fastmcp-simple/fastmcp_simple/agent$ **uv run adk run .**

##You need to usually run other gcloud commands to associate your agent to your cloud project for billing etc)
**gcloud auth application-default login**
**gcloud auth application-default set-quota-project vjindal-project-ai-basic**
**gcloud auth login**