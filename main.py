from agents.planner_agent import plan_task
from agents.research_agent import research
from agents.analysis_agent import analyze
from agents.decision_agent import decide
from memory.memory_store import save_memory

query = "Should a company invest in AI?"

tasks = plan_task(query)
data = research(tasks)
insights = analyze(data)
decision = decide(insights)

save_memory(query, decision)

print(decision)