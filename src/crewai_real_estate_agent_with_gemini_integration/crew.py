from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class CrewaiRealEstateAgentWithGeminiIntegrationCrew():
    """CrewaiRealEstateAgentWithGeminiIntegration crew"""

    @agent
    def PropertySearch(self) -> Agent:
        return Agent(
            config=self.agents_config['PropertySearch'],
            tools=[],
        )

    @agent
    def ListingManager(self) -> Agent:
        return Agent(
            config=self.agents_config['ListingManager'],
            tools=[],
        )

    @agent
    def MarketAnalysis(self) -> Agent:
        return Agent(
            config=self.agents_config['MarketAnalysis'],
            tools=[],
        )

    @agent
    def ChatSupportScheduling(self) -> Agent:
        return Agent(
            config=self.agents_config['ChatSupportScheduling'],
            tools=[],
        )

    @agent
    def DocumentAutomation(self) -> Agent:
        return Agent(
            config=self.agents_config['DocumentAutomation'],
            tools=[],
        )

    @agent
    def VirtualTour(self) -> Agent:
        return Agent(
            config=self.agents_config['VirtualTour'],
            tools=[],
        )

    @agent
    def Personalization(self) -> Agent:
        return Agent(
            config=self.agents_config['Personalization'],
            tools=[],
        )

    @agent
    def NeighborhoodInsights(self) -> Agent:
        return Agent(
            config=self.agents_config['NeighborhoodInsights'],
            tools=[],
        )

    @agent
    def PerformanceMonitoring(self) -> Agent:
        return Agent(
            config=self.agents_config['PerformanceMonitoring'],
            tools=[],
        )

    @agent
    def MeetingSchedulingCalling(self) -> Agent:
        return Agent(
            config=self.agents_config['MeetingSchedulingCalling'],
            tools=[],
        )


    @task
    def property_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['property_search_task'],
            tools=[],
        )

    @task
    def listing_management_task(self) -> Task:
        return Task(
            config=self.tasks_config['listing_management_task'],
            tools=[],
        )

    @task
    def market_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['market_analysis_task'],
            tools=[],
        )

    @task
    def chat_support_scheduling_task(self) -> Task:
        return Task(
            config=self.tasks_config['chat_support_scheduling_task'],
            tools=[],
        )

    @task
    def document_automation_task(self) -> Task:
        return Task(
            config=self.tasks_config['document_automation_task'],
            tools=[],
        )

    @task
    def virtual_tour_task(self) -> Task:
        return Task(
            config=self.tasks_config['virtual_tour_task'],
            tools=[],
        )

    @task
    def personalization_task(self) -> Task:
        return Task(
            config=self.tasks_config['personalization_task'],
            tools=[],
        )

    @task
    def neighborhood_insights_task(self) -> Task:
        return Task(
            config=self.tasks_config['neighborhood_insights_task'],
            tools=[],
        )

    @task
    def performance_monitoring_task(self) -> Task:
        return Task(
            config=self.tasks_config['performance_monitoring_task'],
            tools=[],
        )

    @task
    def meeting_scheduling_calling_task(self) -> Task:
        return Task(
            config=self.tasks_config['meeting_scheduling_calling_task'],
            tools=[],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the CrewaiRealEstateAgentWithGeminiIntegration crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
