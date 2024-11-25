import tkinter as tk
from tkinter import ttk, messagebox, font
from datetime import datetime
import webbrowser

class ModernButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        self.normal_bg = kwargs.pop('bg', '#2196F3')
        self.hover_bg = kwargs.pop('activebackground', '#1976D2')
        self.text_color = kwargs.pop('fg', '#FFFFFF')
        
        super().__init__(master, **kwargs)
        self.configure(
            relief='flat',
            bg=self.normal_bg,
            fg=self.text_color,
            activebackground=self.hover_bg,
            activeforeground='#FFFFFF',
            font=('Helvetica', 12, 'bold'),
            padx=25,
            pady=12,
            cursor='hand2',
            borderwidth=0,
            highlightthickness=1,
            highlightbackground='#333333',
        )
        
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)

    def on_enter(self, event):
        self.configure(bg=self.hover_bg)

    def on_leave(self, event):
        self.configure(bg=self.normal_bg)

class ModernEntry(ttk.Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            font=('Helvetica', 10),
        )

class DavidChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("FUSION2RADIO DJ BOT")
        self.root.geometry("800x700")
        
        # Set dark theme
        self.root.configure(bg='#1a1a1a')
        
        # Chat state
        self.user_name = None
        self.favorite_dj = None
        self.music_preference = None
        self.last_topic = None
        self.conversation_history = []
        
        # Create header frame with gradient effect
        self.header_frame = tk.Frame(self.root, bg='#1a1a1a')
        self.header_frame.pack(fill='x', pady=(20, 0))
        
        # Create title with DJ style
        self.title_label = tk.Label(
            self.header_frame,
            text="FUSION2RADIO",
            font=('Helvetica', 32, 'bold'),
            fg='#00ffff',
            bg='#1a1a1a'
        )
        self.title_label.pack()
        
        # Create subtitle
        self.subtitle = tk.Label(
            self.header_frame,
            text="Professional DJ Services",
            font=('Helvetica', 14),
            fg='#7f7f7f',
            bg='#1a1a1a'
        )
        self.subtitle.pack(pady=(0, 20))
        
        # Create top buttons frame
        self.top_buttons_frame = tk.Frame(self.root, bg='#1a1a1a')
        self.top_buttons_frame.pack(pady=20)
        
        # Create website button
        self.website_button = ModernButton(
            self.top_buttons_frame,
            text="🌐  VISIT WEBSITE",
            command=lambda: webbrowser.open('https://sites.google.com/view/fusion2radio/home'),
            bg='#6200EA',
            activebackground='#7C4DFF',
            fg='#FFFFFF'
        )
        self.website_button.pack(side=tk.LEFT, padx=10)
        
        # Create contact button
        self.contact_button = ModernButton(
            self.top_buttons_frame,
            text="✉  CONTACT US",
            command=lambda: webbrowser.open('mailto:rockmoulds@gmail.com'),
            bg='#00BFA5',
            activebackground='#1DE9B6',
            fg='#FFFFFF'
        )
        self.contact_button.pack(side=tk.LEFT, padx=10)
        
        # Add separator
        separator_frame = tk.Frame(self.root, height=2, bg='#333333')
        separator_frame.pack(fill='x', padx=40, pady=20)
        
        # DJs information
        self.djs = {
            "DJ MICKY": {
                "style": "House and Deep Tech",
                "specialty": "Groovy basslines and infectious rhythms",
                "events": ["Club Night", "Beach Party"],
                "bio": "With over 10 years of experience, DJ MICKY has performed at major festivals across Europe. Known for seamless transitions and crowd-pleasing sets.",
                "residencies": ["The Underground Club", "Sunset Beach"],
                "social_media": {
                    "instagram": "@dj_micky",
                    "soundcloud": "soundcloud.com/djmicky"
                }
            },
            "DJ IPRO": {
                "style": "Techno and Progressive",
                "specialty": "Mind-bending drops and epic buildups",
                "events": ["Warehouse Rave", "Club Night"],
                "bio": "The techno maestro of the underground scene. DJ IPRO brings raw energy and cutting-edge tracks to every set.",
                "residencies": ["The Factory", "The Underground Club"],
                "social_media": {
                    "instagram": "@dj_ipro",
                    "soundcloud": "soundcloud.com/djipro"
                }
            },
            "DJ FUSION": {
                "style": "Tropical House and Chill",
                "specialty": "Smooth transitions and summer vibes",
                "events": ["Beach Party", "Sunday Brunch"],
                "bio": "Creating the perfect atmosphere for any occasion, DJ FUSION specializes in feel-good music that keeps the crowd moving.",
                "residencies": ["Sky Lounge", "Sunset Beach"],
                "social_media": {
                    "instagram": "@dj_fusion",
                    "soundcloud": "soundcloud.com/djfusion"
                }
            }
        }
        
        # Events information
        self.events = {
            "Club Night": {
                "date": "Every Friday",
                "time": "10 PM - 3 AM",
                "location": "The Underground Club",
                "description": "Deep house and techno night featuring DJ MICKY and DJ IPRO",
                "dress_code": "Smart casual, no sportswear",
                "entry": "£15 before 11 PM, £20 after",
                "table_booking": "Available from £200",
                "features": ["2 dance floors", "Premium sound system", "VIP area"]
            },
            "Beach Party": {
                "date": "Every Saturday",
                "time": "4 PM - 10 PM",
                "location": "Sunset Beach",
                "description": "Sunset sessions with DJ FUSION and DJ MICKY",
                "dress_code": "Beach casual",
                "entry": "£10 all night",
                "features": ["Beachfront bar", "Food vendors", "Sunset view"]
            },
            "Warehouse Rave": {
                "date": "Last Saturday of month",
                "time": "11 PM - 6 AM",
                "location": "The Factory",
                "description": "Hard techno and industrial beats with DJ IPRO",
                "dress_code": "No dress code",
                "entry": "£20 standard, £30 VIP",
                "features": ["Laser show", "CO2 cannons", "Multiple rooms"]
            },
            "Sunday Brunch": {
                "date": "Every Sunday",
                "time": "12 PM - 5 PM",
                "location": "Sky Lounge",
                "description": "Relaxed vibes with DJ FUSION",
                "dress_code": "Smart casual",
                "entry": "£25 including brunch buffet",
                "features": ["Rooftop views", "Unlimited prosecco", "Gourmet buffet"]
            }
        }

        # Venues information
        self.venues = {
            "The Underground Club": {
                "capacity": "500 people",
                "location": "123 Main Street, Downtown",
                "features": ["State-of-the-art sound system", "Multiple bars", "VIP booths"],
                "contact": "clubs@fusion2radio.com",
                "dress_code": "Smart casual, no sportswear",
                "opening_hours": "Thu-Sat 10 PM - 3 AM"
            },
            "The Factory": {
                "capacity": "1000 people",
                "location": "45 Industrial Way",
                "features": ["Massive dance floor", "Industrial aesthetics", "Advanced light system"],
                "contact": "factory@fusion2radio.com",
                "dress_code": "No restrictions",
                "opening_hours": "Special events only"
            },
            "Sky Lounge": {
                "capacity": "200 people",
                "location": "Skyline Tower, 20th Floor",
                "features": ["Panoramic city views", "Premium bar", "Restaurant service"],
                "contact": "skylounge@fusion2radio.com",
                "dress_code": "Smart casual",
                "opening_hours": "Wed-Sun 12 PM - 12 AM"
            },
            "Sunset Beach": {
                "capacity": "Outdoor venue",
                "location": "Sunset Beach Boulevard",
                "features": ["Beachfront location", "Open-air dance floor", "Food vendors"],
                "contact": "beach@fusion2radio.com",
                "dress_code": "Beach casual",
                "opening_hours": "Weather dependent, check website"
            }
        }

        # Website features
        self.website_info = {
            "url": "https://sites.google.com/view/fusion2radio/home",
            "features": {
                "Event Calendar": "Browse and book upcoming events",
                "DJ Profiles": "Learn about our resident and guest DJs",
                "Photo Gallery": "Event photos and memorable moments",
                "Table Booking": "Reserve VIP tables and booths",
                "Membership": "Join our VIP membership program",
                "Music": "Listen to our DJs' latest mixes",
                "Blog": "Latest news and event reviews"
            },
            "social_media": {
                "Instagram": "@fusion2radio",
                "Facebook": "Fusion2RadioOfficial",
                "Twitter": "@fusion2radio",
                "YouTube": "Fusion2RadioTV"
            },
            "contact": {
                "General": "info@fusion2radio.com",
                "Bookings": "bookings@fusion2radio.com",
                "Press": "press@fusion2radio.com"
            }
        }
        
        self.setup_gui()
        self.initialize_chat()
    
    def setup_gui(self):
        # Create chat display
        self.chat_frame = tk.Frame(self.root, bg='#1a1a1a')
        self.chat_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.chat_display = tk.Text(
            self.chat_frame,
            wrap=tk.WORD,
            bg='#2d2d2d',
            fg='#ffffff',
            font=('Helvetica', 10),
            padx=10,
            pady=10,
            state='disabled',
            relief='flat',
            highlightthickness=1,
            highlightbackground='#333333'
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        
        # Create input frame
        self.input_frame = tk.Frame(self.root, bg='#1a1a1a')
        self.input_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        self.user_input = ModernEntry(self.input_frame)
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.user_input.bind('<Return>', lambda e: self.send_message())
        
        self.send_button = ModernButton(
            self.input_frame,
            text="SEND",
            command=self.send_message,
            bg='#00C853',
            activebackground='#00E676'
        )
        self.send_button.pack(side=tk.RIGHT)
    
    def initialize_chat(self):
        welcome_message = ("👋 Hey there! I'm David, your FUSION2RADIO assistant!\n\n"
                         "I'd love to get to know you better! What's your name?")
        self.display_message("David", welcome_message)
        self.last_topic = "greeting"

    def send_message(self):
        user_message = self.user_input.get().strip()
        if not user_message:
            return
        
        self.display_message("You", user_message)
        self.user_input.delete(0, tk.END)
        
        # Process user message and get response
        response = self.get_response(user_message.lower())
        self.display_message("Bot", response)
    
    def display_message(self, sender, message):
        self.chat_display.configure(state='normal')
        timestamp = datetime.now().strftime("%H:%M")
        
        if sender == "You":
            self.chat_display.insert(tk.END, f"\n{timestamp} {sender}: ", "user")
        else:
            self.chat_display.insert(tk.END, f"\n{timestamp} {sender}: ", "bot")
            
        self.chat_display.insert(tk.END, f"{message}\n")
        self.chat_display.configure(state='disabled')
        self.chat_display.see(tk.END)
    
    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        self.conversation_history.append(("user", user_input))
        
        # If we don't have the user's name yet, get it first
        if not self.user_name and self.last_topic == "greeting":
            self.user_name = user_input.title()
            response = (f"Great to meet you, {self.user_name}! 😊\n\n"
                      f"I'm here to help you discover amazing music and events! "
                      f"Are you into any particular style of electronic music? "
                      f"We've got everything from House to Techno to Tropical vibes!")
            self.last_topic = "music_preference"
            return response
            
        # If we're asking about music preference
        if self.last_topic == "music_preference":
            self.music_preference = user_input
            # Look for matching DJs based on music preference
            matching_djs = []
            for dj, info in self.djs.items():
                if any(style.lower() in user_input for style in info['style'].lower().split()):
                    matching_djs.append(dj)
            
            if matching_djs:
                self.favorite_dj = matching_djs[0]
                response = (f"Awesome choice, {self.user_name}! 🎵 You'll love {', '.join(matching_djs)}!\n\n"
                          f"Would you like to:\n"
                          f"1. Learn more about these DJs\n"
                          f"2. Check out their upcoming events\n"
                          f"3. Listen to their latest mixes\n"
                          f"Just let me know what interests you!")
            else:
                response = (f"That's cool, {self.user_name}! We have a great variety of music styles.\n\n"
                          f"What would you like to explore first?\n"
                          f"• Our amazing DJs and their styles\n"
                          f"• Upcoming events and parties\n"
                          f"• Different venues and their vibes")
            self.last_topic = "interests"
            return response

        # Check for goodbyes
        if any(word in user_input for word in ["bye", "goodbye", "see you", "cya"]):
            return self.get_goodbye_message()

        # Check for thank you messages
        if any(word in user_input for word in ["thank", "thanks", "thx"]):
            return self.get_thank_you_response()

        # Regular keyword responses with context
        if "dj" in user_input:
            self.last_topic = "djs"
            return self.get_dj_info_with_context()
        elif "event" in user_input or "party" in user_input:
            self.last_topic = "events"
            return self.get_event_info_with_context()
        elif "club" in user_input or "venue" in user_input:
            self.last_topic = "venues"
            return self.get_venue_info_with_context()
        elif "book" in user_input:
            self.last_topic = "booking"
            return self.get_booking_info_with_context()
        elif "website" in user_input:
            self.last_topic = "website"
            return self.get_website_info_with_context()
        elif "contact" in user_input:
            self.last_topic = "contact"
            return self.get_contact_info_with_context()
        elif "music" in user_input or "style" in user_input:
            self.last_topic = "music"
            return self.get_music_info_with_context()
        elif any(word in user_input for word in ["hello", "hi", "hey", "sup"]):
            if self.user_name:
                return f"Hey again, {self.user_name}! 👋 What can I help you with today?"
            else:
                return self.get_greeting_with_context()
        else:
            return self.get_contextual_help_message()

    def get_dj_info_with_context(self):
        base_response = "🎧 Let me tell you about our amazing DJs:\n\n"
        
        for dj, info in self.djs.items():
            base_response += f"✨ {dj}\n"
            base_response += f"Style: {info['style']}\n"
            base_response += f"Specialty: {info['specialty']}\n"
            base_response += f"Bio: {info['bio']}\n"
            base_response += f"Residencies: {', '.join(info['residencies'])}\n"
            base_response += f"Find them on: {', '.join([f'{platform}: {handle}' for platform, handle in info['social_media'].items()])}\n\n"
        
        if self.user_name and self.music_preference:
            base_response += f"\nBased on your interest in {self.music_preference}, {self.user_name}, "
            base_response += "you might particularly enjoy our upcoming events! Want to hear about them? 🎉"
        else:
            base_response += "\nWant to know about their upcoming events? Just ask! 🎉"
        
        return base_response

    def get_event_info_with_context(self):
        base_response = "🎉 Here's what's coming up:\n\n"
        
        for event, info in self.events.items():
            base_response += f"✨ {event}\n"
            base_response += f"When: {info['date']} at {info['time']}\n"
            base_response += f"Where: {info['location']}\n"
            base_response += f"Details: {info['description']}\n"
            base_response += f"Dress Code: {info['dress_code']}\n"
            base_response += f"Entry: {info['entry']}\n"
            base_response += f"Features: {', '.join(info['features'])}\n\n"
        
        if self.user_name:
            base_response += f"\nHey {self.user_name}, would you like to know about table bookings or VIP access? 🎵"
        else:
            base_response += "\nInterested in making a booking? Just ask! 🎵"
        
        return base_response

    def get_venue_info_with_context(self):
        base_response = "🏢 Check out our amazing venues:\n\n"
        
        for venue, info in self.venues.items():
            base_response += f"✨ {venue}\n"
            base_response += f"Capacity: {info['capacity']}\n"
            base_response += f"Location: {info['location']}\n"
            base_response += f"Features: {', '.join(info['features'])}\n"
            base_response += f"Dress Code: {info['dress_code']}\n"
            base_response += f"Opening Hours: {info['opening_hours']}\n"
            base_response += f"Contact: {info['contact']}\n\n"
        
        if self.user_name:
            base_response += f"\n{self.user_name}, would you like to know about upcoming events at any of these venues? 🎉"
        else:
            base_response += "\nWant to know what's happening at these venues? Just ask! 🎉"
        
        return base_response

    def get_booking_info_with_context(self):
        response = "🎟️ Here's how you can make bookings:\n\n"
        response += "🎧 DJ Bookings: bookings@fusion2radio.com\n"
        response += "🏢 Table Reservations: Visit our website's booking section\n"
        response += "💎 VIP Services: Contact our VIP team at vip@fusion2radio.com\n\n"
        
        if self.user_name and self.favorite_dj:
            response += f"By the way {self.user_name}, {self.favorite_dj} has some amazing events coming up! "
            response += "Would you like to hear about them? 🎉"
        else:
            response += "Want to know about upcoming events? Just ask! 🎉"
        
        return response

    def get_website_info_with_context(self):
        response = "🌐 Check out our website: " + self.website_info['url'] + "\n\n"
        response += "Here's what you can do there:\n"
        for feature, desc in self.website_info['features'].items():
            response += f"✨ {feature}: {desc}\n"
        
        response += "\nStay connected on social media:\n"
        for platform, handle in self.website_info['social_media'].items():
            response += f"📱 {platform}: {handle}\n"
        
        if self.user_name:
            response += f"\n{self.user_name}, would you like me to help you find something specific on our website? 😊"
        
        return response

    def get_music_info_with_context(self):
        response = "🎵 Our music styles:\n\n"
        response += "🎧 House & Deep Tech - Perfect for club nights\n"
        response += "🎧 Techno & Progressive - High-energy warehouse vibes\n"
        response += "🎧 Tropical House - Ideal for beach parties\n"
        response += "🎧 Chill & Lounge - Sunday brunch atmosphere\n\n"
        
        if self.user_name and self.music_preference:
            response += f"Since you're into {self.music_preference}, {self.user_name}, "
            response += "I can recommend some specific events you might love! Interested? 🎉"
        else:
            response += "Want to know which DJs play your favorite style? Just ask! 🎉"
        
        return response

    def get_goodbye_message(self):
        if self.user_name:
            return f"Goodbye, {self.user_name}! 👋 Hope to see you at one of our events soon! Feel free to come back if you need anything else! 🎉"
        return "Goodbye! 👋 Hope to see you at one of our events soon! Feel free to come back if you need anything else! 🎉"

    def get_thank_you_response(self):
        if self.user_name:
            return f"You're welcome, {self.user_name}! 😊 Is there anything else you'd like to know about? I'm here to help!"
        return "You're welcome! 😊 Is there anything else you'd like to know about? I'm here to help!"

    def get_greeting_with_context(self):
        return "Hey there! 👋 I'm David, your FUSION2RADIO assistant! What's your name? 😊"

    def get_contextual_help_message(self):
        base_response = "I'm here to help! You can ask me about:\n\n"
        base_response += "• Our DJs and their music styles 🎧\n"
        base_response += "• Upcoming events and parties 🎉\n"
        base_response += "• Venue information and bookings 🏢\n"
        base_response += "• Website features and contact details 🌐\n\n"
        
        if self.user_name:
            base_response += f"What interests you most, {self.user_name}? 😊"
        else:
            base_response += "What would you like to know about? 😊"
        
        return base_response

def main():
    root = tk.Tk()
    app = DavidChatbot(root)
    root.mainloop()

if __name__ == "__main__":
    main()
