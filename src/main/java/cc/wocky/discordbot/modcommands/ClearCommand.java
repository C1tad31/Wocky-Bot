package cc.wocky.discordbot.modcommands;

import cc.wocky.discordbot.utils.MessageEmbed;
import net.dv8tion.jda.api.Permission;
import net.dv8tion.jda.api.entities.*;
import net.dv8tion.jda.api.events.interaction.command.SlashCommandInteractionEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

import java.time.Instant;
import java.util.List;

import org.jetbrains.annotations.NotNull;

public class ClearCommand extends ListenerAdapter {
    @Override
    public void onSlashCommandInteraction(@NotNull SlashCommandInteractionEvent event) {
        Member member = event.getMember();
        if (event.getName().equals("clear")) {
            if (!member.hasPermission(Permission.MESSAGE_MANAGE) || !member.hasPermission(Permission.ADMINISTRATOR)) {
                event.reply("You dont have the required permission to use this command!").setEphemeral(true).queue();
            } else {
                int amount = event.getOption("amount").getAsInt();
                MessageChannel channel = event.getOption("channel").getAsMessageChannel();

                MessageHistory history = new MessageHistory(channel);
                List<Message> msg = history.retrievePast(amount).complete();

                event.getChannel().purgeMessages(msg);
                MessageEmbed.createEmbed(event, "reg", member, "Messages Cleared!", "https://wocky.cc/", null, "" + amount + " messages have been cleared from the specified channel!", event.getGuild().getIconUrl(), "#000000", Instant.now(), "Wocky Bot | Made by: Citadel");
            }
        }
    }
}
