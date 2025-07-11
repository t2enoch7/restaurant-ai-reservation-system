```
restaurant-ai-poc/
├── app/
│   ├── agents/
│   │   ├── orchestrator_agent.py        
│   │   ├── reservation_agent.py
│   │   ├── table_agent.py
│   │   └── guest_agent.py
│   ├── cli/
│   │   └── sync_tools.py                
│   ├── models/
│   │   ├── guest_model.py
│   │   ├── reservation_model.py
│   │   └── table_model.py
│   ├── routes/
│   │   ├── guest_routes.py
│   │   ├── reservation_routes.py
│   │   └── table_routes.py
│   ├── services/
│   │   ├── guest_service.py
│   │   ├── reservation_service.py
│   │   └── table_service.py
│   ├── tools/
│   │   ├── agent_manifest.json          
│   │   └── tool_definitions.json       
│   ├── websocket/
│   │   └── table_ws.py                  
│   └── main.py                        
├── docker-compose.yml                  
├── Dockerfile                         
├── requirements.txt                   
├── requirements-dev.txt               
├── .env                              
└── .github/
    └── workflows/
        └── deploy.yml      
```
