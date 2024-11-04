# brightSPARK Labs Reverse Proxy

An `appcli` based project for standing up a reverse proxy to manage traffic for multiple `docker-compose` projects running on the same machine.

## Overview

```mermaid
  graph TD

    U["User"]

    %% Reverse Proxy stack.
    subgraph RP ["Reverse Proxy"]
        P["Proxy"]
    end

    %% StackX
    subgraph SX ["StackX"]
        A["AppA"]
        B["AppB"]
    end

    %% StackY
    subgraph SY ["StackY"]
        C["AppC"]
        D["AppD"]
    end

    %% Edges
    U -->|"https#58;//mydomain.example.com"| P
    P -->|"http#58;//appa.stackx:8080"| A
    P -->|"http#58;//appb.stackx:5432"| B
    P -->|"http#58;//appc.stacky:8080"| C
    P -->|"http#58;//appc.stacky:1234"| D
```

## Configuration