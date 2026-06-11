class DutyService:
    def __init__(self, repository):
        self.repository = repository

        # TEMPORARY; Flask still depends on this attribute
        # Will be removed once Duties API fully migrates to repository
        self.duties = self.repository.get_all_duties()

    def create_duty(self, number, description):
        return self.repository.create_duty(
            number,
            description
        )
    
    def get_all_duties(self):
        return self.repository.get_all_duties()