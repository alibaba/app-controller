class ProgressTracker:
    def __init__(self, total_count, update_interval_percent=0.1, display_char='*', display_text="Processed"):
        self.total_count = total_count
        self.update_interval_percent = update_interval_percent
        self.update_interval_count = self.total_count * update_interval_percent

        self.current_count = 0
        self.next_update_count = self.update_interval_count
        self.display_char = display_char
        self.display_text = display_text

    def update(self, new_count):
        self.current_count += new_count
        if self.current_count >= self.next_update_count or self.current_count >= self.total_count:
            self.next_update_count += self.update_interval_count
            self.print_progress()

    def print_progress(self):
        progress_percent = (self.current_count / self.total_count) * 100
        num_display_chars = int((progress_percent / 100) * 30)  # 30 is the length of the progress bar
        progress_bar = self.display_char * num_display_chars
        print(f"{self.display_text} {progress_percent:.2f}% [{progress_bar}]")

    def finish(self):
        self.update(self.total_count - self.current_count)
