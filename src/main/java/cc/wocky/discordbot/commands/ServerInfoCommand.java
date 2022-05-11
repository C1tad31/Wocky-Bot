package cc.wocky.discordbot.commands;

import cc.wocky.discordbot.utils.MessageEmbed;
import net.dv8tion.jda.api.entities.Member;
import net.dv8tion.jda.api.events.interaction.command.SlashCommandInteractionEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import org.jetbrains.annotations.NotNull;

import java.time.Instant;

public class ServerInfoCommand extends ListenerAdapter {

    @Override
    public void onSlashCommandInteraction(@NotNull SlashCommandInteractionEvent event) {
        if (event.getName().equals("serverinfo")) {
            Member member = event.getMember();
            MessageEmbed.createEmbed(
                    event,
                    "reg",
                    member,
                    "Server Info",
                    "https://wocky.cc/",
                    null,
                    String.format("Server Owner: %s\nServer ID: %s\nServer Icon URL: %s\n", event.getGuild().getOwner(), event.getGuild().getId(), event.getGuild().getIconUrl()),
                    event.getGuild().getIconUrl(),
                    "#000000",
                    Instant.now(),
                    "Wocky Bot | Made By: Citadel");
        }
    }
}
