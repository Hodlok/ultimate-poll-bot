"""Admin related callback handler."""
import time

from pollbot.i18n import i18n
from pollbot.helper.plot import send_plots
from pollbot.helper.update import update_poll_messages
from pollbot.telegram.keyboard import get_admin_settings_keyboard
from pollbot.models import Poll
from pollbot.display.admin import stats


def open_admin_settings(session, context):
    """Open the main menu."""
    keyboard = get_admin_settings_keyboard(context.user)
    context.query.message.edit_text(
        stats(session),
        reply_markup=keyboard,
        parse_mode='Markdown',
        disable_web_page_preview=True,
    )


def update_all(session, context):
    """Update all polls."""
    chat = context.query.message.chat

    updated = 0
    poll_count = session.query(Poll) \
        .filter(Poll.created.is_(True)) \
        .count()
    chat.send_message(f'Updating {poll_count} polls')
    print(f'Updating {poll_count} polls')

    while updated < poll_count:
        polls = session.query(Poll) \
            .filter(Poll.created.is_(True)) \
            .order_by(Poll.id.desc()) \
            .offset(updated) \
            .limit(100) \
            .all()

        if updated % 500 == 0:
            chat.send_message(f'Updated {updated} polls')
        updated += len(polls)

        for poll in polls:
            update_poll_messages(session, context.bot, poll)
            time.sleep(0.2)

    return "Done"


def plot(session, context):
    """Plot interesting statistics."""
    send_plots(session, context.query.message.chat)
