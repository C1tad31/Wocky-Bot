package cc.wocky.discordbot.modcommands;

import net.dv8tion.jda.api.Permission;
import net.dv8tion.jda.api.entities.Member;
import net.dv8tion.jda.api.events.interaction.command.SlashCommandInteractionEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

import java.time.Instant;

import org.jetbrains.annotations.NotNull;

import cc.wocky.discordbot.utils.MessageEmbed;

public class BanCommand extends ListenerAdapter {
    @Override
    public void onSlashCommandInteraction(@NotNull SlashCommandInteractionEvent event) {
        Member member = event.getMember();
        if (event.getName().equals("ban")) {
            if (!member.hasPermission(Permission.BAN_MEMBERS) || !member.hasPermission(Permission.ADMINISTRATOR)) {
                event.reply("You dont have the required permission to use this command!").setEphemeral(true).queue();
            } else {
                Member target = event.getOption("member").getAsMember();
                String reason  = event.getOption("reason").getAsString();

                target.ban(1, reason).queue();
                MessageEmbed.createEmbed(event, "eph", member, "Member Banned!", "https://wocky.cc/", null, target.getAsMention() + " has been banned by: " + member.getAsMention() + "\nReason: " + reason, event.getGuild().getIconUrl(), "#000000", Instant.now(), "WockyBot | Made by: Citadel");
            }
        }
    }
}
