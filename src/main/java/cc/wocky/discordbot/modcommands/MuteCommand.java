package cc.wocky.discordbot.modcommands;

import net.dv8tion.jda.api.Permission;
import net.dv8tion.jda.api.entities.Member;
import net.dv8tion.jda.api.entities.Role;
import net.dv8tion.jda.api.events.interaction.command.SlashCommandInteractionEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

import java.time.Instant;
import java.util.Objects;

import org.jetbrains.annotations.NotNull;

import cc.wocky.discordbot.utils.MessageEmbed;

public class MuteCommand extends ListenerAdapter {
    @Override
    public void onSlashCommandInteraction(@NotNull SlashCommandInteractionEvent event) {
        Member member = event.getMember();
        if (event.getName().equals("mute")) {
            if (!member.hasPermission(Permission.MANAGE_ROLES) || !member.hasPermission(Permission.ADMINISTRATOR)) {
                event.reply("You dont have the required permission to use this command!").setEphemeral(true).queue();
            } else {
                Member target = Objects.requireNonNull(event.getOption("member")).getAsMember();
                Role role = Objects.requireNonNull(event.getGuild()).getRolesByName("Muted", true).get(0);
                assert target != null;
                event.getGuild().addRoleToMember(target, role).queue();

                MessageEmbed.createEmbed(event, "eph", member, "Member Muted!", "https://wocky.cc/", null, target.getAsMention() + " has been muted by: " + member.getAsMention(), event.getGuild().getIconUrl(), "#000000", Instant.now(), "Wocky Bot | Made by: Citadel");
            }
        }
    }
}
