---
title: MAI 7002 NOTE
date: 2023-10-27 20:00:00
tags: [Notion, 笔记]
categories: [MAI]
index_img: /img/7002notecover.jpg  # (可选) Fluid主题支持配置封面图
---


# MAI 7002 NOTE

# WEEK 1

## what is artificial intelligence?

AI simulates human intelligence processes in computer science.

AI's core capabilities encompass **learning** to acquire information, **reasoning** to reach conclusions, **self-correction** through feedback, **pattern recognition** in data, and **decision-making** to select optimal actions.

## Types of AI systems

Narrow AI (Week AI) General AI Super AI

## AI history

## The Turing Test: A benchmark for intelligence

The test involves an interrogator(询问者) with both a human and a machine, attempting to identify which is whitch.

## Symbolic AI: The dominant Paradigm

## Expert Systems Renaissance

## The 2012 ImageNet Breakthrough: **AlexNet Revolution**

# WEEK2 AI AGENTS

## What is an Agent?

anything that perceives its environment (through sensors) and acts upon it (through actuators) to achieve goals

## Environment types

可观测性	Fully vs. Partially Observable: 代理能否看到环境的完整状态。
确定性	Deterministic vs. Stochastic: 下一个状态是否完全由当前状态和动作决定（无随机性）。
时间结构	Episodic vs. Sequential: 动作影响是否仅限于当前回合（Episodic）还是会影响未来（Sequential）。
变化性	Static vs. Dynamic: 在代理决策时，环境是否会自己发生变化。
状态/动作	Discrete vs. Continuous: 状态、动作或时间是有限可数的还是连续无限的。
代理数量	Single vs. Multi-agent: 环境中是否只有一个智能代理。

## PEAS Framework

specify the performance measure, the environment, and the agent’s actuators and sensors ➔ PEAS Framework

## AI SOFTWARE AGENTS

AI MODULE/ AI AGENT /environment & system

### agentic AI

complex tasks/ proactivity / minimizing human supervision / better use of tools and knowledge

### LLM-Based Agents

- the ReAct Loop Reasong + Act
- Reflexion Pattern (Self-Reflection and self-Correction)
- Retrieval-Augmented Generation (RAG)
    - 2 major limitations
        - knowledge cutoff
        - hallucinations
    - RAG is an AI agent that can retrieve(检索) relevant information from a knowledge base and use that information to ground its responses.
        - offline indexing
        - online retrieval + Generation
    - embedding model
    

### TRY AUG

prepare knowledge base

import TfidfVectorizer - Create TF-IDF vectorizer and fit it on our documents

simulates scores = doc_vectors * query_vec.T

retrieve the top document for each query

# UNINFORMED & INFORMED SEARCH

## Uninformed Search

### BFS -  Breadth First Search

```python
visited = set()
queue = []
def BFS(visited,node,graph):
	visited.append(node)
	queue.append(node)
	
	while queue:
		m=queue.pop(0)
		print(m,end = "")
		for neighbour in graph[m]:
			if neighbour not in visited:
				visited.append(neighbour)
				queue.append(neighbour)
				# first in firt out
```

### Depth First Search

```python
visited = set()
goal_found = false

def DFS(visited,node,graph,goal):
	global goal_found
	if goal_found = true:
		return
	if node not in visited:
		visited.add(node)
		if node == goal:
			goal_found = true 
			return
		for neighbour in graph[node]:
			DFS(visited,graph,neghbour,goal)
```

### Depth Limited Search

```python
def dls(graph: Graph, start: str, goal: str, limit: int):
    """Depth Limited Search. Return (order, path)"""
    # Hints:
    # Use recursion with a depth parameter that decrements on each edge.
    # Track a parent map like BFS/DFS to rebuild a path when you find 'goal'.
    # Stop exploring a branch when limit < 0.
    visited = set()
    order = []
    parent: dict[str, Optional[str]] = {start:None}
    found = False

    def rec(u:str,limit):
        nonlocal found
        if limit<0 or found:
            return  
        
        visited.add(u)
        order.append(u)
        if u == goal:
            found = True
            return
        for v in graph.get(u,[]):
            if v not in visited:
                parent[v] = u
                rec(v,limit-1)

    rec(start, limit)
    return order, reconstruct_path(parent, start, goal)
    
```

### Iterative Deepening Search

Combination of DFS and BFS

### Uniform Cost Search

Explores paths with the lowest cumulative cost.

### Bidirectional Search

use two simultaneous searches: from the start and from the goal.

## Informed Search

### Heuristics Function 启发函数

### Best-first Search

● f(n) = estimated total cost of path through n to goal

● h(n) = estimated cost from n to goal (heuristic)

find min h(n)

### A* Search

<aside>
<img src="https://www.notion.so/icons/arrow-right-line_green.svg" alt="https://www.notion.so/icons/arrow-right-line_green.svg" width="40px" />

f(n) = g(n) + h(n) 
g(n) = cost so far to reach n 
h(n) = estimated cost from n to goal (heuristic) 
f(n) = estimated total cost of path through n to goal 

</aside>

### Game Search

- MiniMax
- Alpha-beta

# WEEK5 Knowledge Representation & Reasoning

## Knowledge Representation

Converts facts, concepts, and relationships into structures to be used by algorithms.

Knowledge Representation transforms data into structured knowledge: concepts, relations, rules, and constraints.

## Types of Knowledge

- Declarative knowledge - what
- Procedural knowledge - how
- Meta-knowledge
- Heuristic knowledge - experience-based
- Common-Sense Knowledge
- Domain-Specific Knowledge

## Techniques of Knowledge Representation

- Logical Representation
    - Captures facts and rules in a precise,
        - Propositional Logic A ∧ B → C
        - FirstOrder Logic (FOL)
            
            Extends propositional logic by introducing variables (x, y, z),
            
            quantifiers (∀, ∃), and predicates (brother, father, human)
            
- Probabilistic models
    
    Bayes Networks Example 
    
- Structured Representations
    - Semantic networks
    - Frames
    - Ontologies

## Ontologies

TBox includes the concepts and relations of the ontology. 
ABox includes the realisations (instances) of concepts and the relations between them

Reasoning can be used to infer new knowledge. 

### Ontology Operations Using Text

- Ontology Learning
- Ontology Enrichment
- Ontology Population

## Reasoning in AI

- deductive reasoning
- inductive reasoning
- abductive reasoning
- Non Monotonic reasoning
-