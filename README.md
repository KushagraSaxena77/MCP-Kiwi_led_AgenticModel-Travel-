# Kiwi MCP Travel Agent

An AI powered travel assistant built with Python, LangChain, LangGraph, Google Gemini, Tavily, and the Kiwi.com MCP server.

The agent understands natural language travel requests and can use external tools to search for real flight options and travel related information. Instead of requiring users to interact with a flight search interface manually, the agent allows them to describe their requirements conversationally.

For example:

> Find me a flight from New Delhi to Mumbai on 12 October, 2026, for a single adult.

The agent can interpret the request, use the Kiwi MCP tools to search for suitable flights, and return the available options in a structured response.




<img width="1117" height="686" alt="image" src="https://github.com/user-attachments/assets/66c160da-c381-4c88-849d-a0d3837dcb27" />

---

## Features

### Natural Language Travel Search

Users can communicate with the travel agent using ordinary language.

Examples:

```text
Find me a flight from New Delhi to Mumbai on 8 October.
```

```text
Find the cheapest direct flight from Delhi to Mumbai tomorrow.
```

```text
I need an afternoon flight from New Delhi to Mumbai.
```

The agent interprets the user's request and determines which tools are required.

### Kiwi.com MCP Integration

The project uses the Kiwi.com MCP server to access flight search functionality through the Model Context Protocol.

This allows the AI agent to interact with flight search tools without implementing the flight search API directly inside the application.

The MCP tools are dynamically loaded using:

```python
mcp_tools = await client.get_tools()
```

### Google Gemini

Google Gemini acts as the language model powering the travel agent.

The model is responsible for:

- Understanding user requests
- Determining when tools are required
- Selecting appropriate tools
- Interpreting tool results
- Generating the final response

### Tavily Web Search

Tavily is included as a web search tool for travel related information that may require additional web research.

The agent can therefore combine structured flight information with general web information when necessary.

### Asynchronous Architecture

The project uses Python's asynchronous programming model throughout the agent workflow.

Key operations use:

```python
await client.get_tools()
```

and:

```python
await agent.ainvoke(...)
```

This is particularly appropriate for the project because the application communicates with multiple external services.

### LangGraph Compatible

The agent is built using LangChain's `create_agent`, which provides a LangGraph based agent runtime.

The project also includes a `langgraph.json` configuration for running the agent through the LangGraph development server.

---

## Architecture


```text
                         User
                           |
                           v
                    +--------------+
                    |   main.py    |
                    | CLI Interface|
                    +------+-------+
                           |
                           v
                    +--------------+
                    |   LangChain  |
                    |    Agent     |
                    +------+-------+
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
       +-----------+ +-----------+ +-----------+
       |   Gemini  | | Kiwi MCP  | |  Tavily  |
       |    LLM    | |   Server  | |   Search |
       +-----------+ +-----------+ +-----------+
             |             |             |
             |             v             |
             |       Flight Search       |
             |                           |
             +-------------+-------------+
                           |
                           v
                    Final Response
                           |
                           v
                         User
```

---


## Project Structure

```text
Kiwi MCP led Agent/
│
├── agent.py
├── main.py
├── langgraph.json
├── .env
├── pyproject.toml
└── README.md
```

### `agent.py`

Contains the core AI agent configuration.

Responsibilities include:

- Loading environment variables
- Configuring Tavily
- Configuring Google Gemini
- Configuring the Kiwi MCP client
- Defining the web search tool
- Defining the travel agent
- Loading MCP tools

### `main.py`

Contains the command line interface.

Responsibilities include:

- Starting the application
- Accepting user input
- Sending requests to the agent
- Displaying the final response
- Maintaining the interactive conversation loop

### `langgraph.json`

Contains the configuration required to run the agent with LangGraph.

Example:

```json
{
  "dependencies": ["."],
  "graphs": {
    "kiwi_mcp_travelAgent": "./agent.py:build_Agent"
  },
  "env": ".env"
}
```


---

## Running with LangGraph

The project can also be launched using the LangGraph development server.

Run:

```bash
uv run langgraph dev
```

LangGraph will start the local development environment and expose the configured travel agent.

The configured graph is:

```text
kiwi_mcp_travelAgent
```

This allows the agent to be inspected and tested through the LangGraph development environment.

---

## Example

### User

```text
Find me a seat from New Delhi to Mumbai on 8 October.
```

### Agent

The agent can search available flights through the Kiwi MCP server and return information such as:

```text
Route
Departure time
Arrival time
Journey duration
Cabin
Price
Booking link
```

The exact results depend on live flight availability.


<img width="427" height="464" alt="image" src="https://github.com/user-attachments/assets/20edff5e-d626-47ec-a2dc-eab91a903a09" />


---



## Agent Design

The travel agent follows a tool using architecture.

```text
                    User Request
                         |
                         v
                   Gemini Agent
                         |
              +----------+----------+
              |                     |
              v                     v
          Kiwi MCP               Tavily
              |                     |
              v                     v
        Flight Search          Web Search
              |                     |
              +----------+----------+
                         |
                         v
                   Gemini Agent
                         |
                         v
                  Final Response
```

The language model decides which tool is appropriate based on the user's request.



---

## Author

Developed by Kushagra Saxena.

This project was created as an exploration of AI agents, MCP based tool integration, LangChain, LangGraph, and intelligent travel automation.

---

## License

This project is intended for educational and development purposes.
