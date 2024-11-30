import { Calendar } from 'https://cdn.jsdelivr.net/npm/@fullcalendar/core@6.1.8/index.global.min.js';
import timeGridPlugin from 'https://cdn.jsdelivr.net/npm/@fullcalendar/timegrid@6.1.8/index.global.min.js';

document.addEventListener('DOMContentLoaded', function () {
const schedulerElement = document.getElementById('scheduler');

const calendar = new Calendar(schedulerElement, {
    plugins: [timeGridPlugin],
    initialView: 'timeGridWeek', // Default to weekly view
    headerToolbar: {
        left: 'prev,next today',
        center: 'title',
        right: 'timeGridDay,timeGridWeek'
    },
    slotMinTime: '08:00:00', // Start time of the grid
    slotMaxTime: '20:00:00', // End time of the grid
    weekends: true, // Show weekends
    editable: true, // Allow drag-and-drop
    selectable: true, // Allow selecting time slots
    eventClick: function (info) {
        alert('Event: ' + info.event.title);
    },
    select: function (info) {
        const title = prompt('Enter event title:');
        if (title) {
            calendar.addEvent({
                title: title,
                start: info.start,
                end: info.end,
                allDay: info.allDay
            });
        }
        calendar.unselect();
    },
    events: [
        {
            title: 'Meeting',
            start: new Date().toISOString().split('T')[0] + 'T10:00:00',
            end: new Date().toISOString().split('T')[0] + 'T12:00:00'
        },
        {
            title: 'Lunch Break',
            start: new Date().toISOString().split('T')[0] + 'T13:00:00',
            end: new Date().toISOString().split('T')[0] + 'T14:00:00'
        }
    ]
});

calendar.render();
});
