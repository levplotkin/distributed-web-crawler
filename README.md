flowchart

seed  -.->|initial url| url_queue 
url_queue  -.->|urls for processing| worker
worker  -.-> |new urls|url_queue
worker  -.-> |update|url_registry
url_registry -.-> |check| worker 
worker  -.-> web

subgraph crawler
seed & worker 
end

subgraph distibuted_crawler
crawler & url_queue & url_registry
end

subgraph web
end
