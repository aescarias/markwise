class HeadingLevelTooHigh(Exception):
    def __str__(self):
        return "Heading level must be lower or equal to 6."
