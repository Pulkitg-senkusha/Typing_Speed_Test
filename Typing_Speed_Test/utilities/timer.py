import time

def start_timer(self, event=None):
        if not self.timer_running:
            self.start_time = time.time()
            self.timer_running = True
            self.update_timer()

def update_timer(self):
        if self.timer_running:
            elapsed = time.time() - self.start_time
            self.timer_label.config(text=f"Time: {elapsed:.1f}s")
            self.root.after(100, self.update_timer)