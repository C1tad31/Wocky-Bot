package cc.wocky.discordbot.commands;

import cc.wocky.discordbot.utils.MessageEmbed;
import net.dv8tion.jda.api.entities.Member;
import net.dv8tion.jda.api.events.interaction.command.SlashCommandInteractionEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import org.jetbrains.annotations.NotNull;

import java.time.Instant;

public class HelpCommand extends ListenerAdapter {
    @Override
    public void onSlashCommandInteraction(@NotNull SlashCommandInteractionEvent event) {
        Member member = event.getMember();
        if (event.getName().equals("help")) {
            MessageEmbed.createEmbed(event,
                    "reg",
                    member,
                    "Wocky Bot",
                    "https://wocky.cc/",
                    null,
                    "```======\nUser Commands\n======\n/help: Displays this menu\n/serverinfo: Displays general information on the server\n/userinfo: Displays user information on a mentioned user\n" +
                            "======\nModeration Commands\n======\n/clear: clears messages from the server\n/kick: Kick a mentioned user from the server\n/ban: Ban a mentioned user from the server\n/mute: Mute a mentioned user in the server\n/unmute: Unmute a mentioned user in the server" +
                            "\n/lockdown: Prevents users from messaging in a channel until unlocked\n/unlock: Unlock a locked channel```",
                    null,
                    "#000000",
                    Instant.now(),
                    "Wocky Bot | Made by: Citadel");
        }
    }
}
