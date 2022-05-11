package cc.wocky.discordbot.modcommands;

import net.dv8tion.jda.api.Permission;
import net.dv8tion.jda.api.entities.Member;
import net.dv8tion.jda.api.entities.MessageChannel;
import net.dv8tion.jda.api.events.interaction.command.SlashCommandInteractionEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import net.dv8tion.jda.internal.utils.PermissionUtil;
import org.jetbrains.annotations.NotNull;

import java.util.Objects;

public class NukeCommand extends ListenerAdapter {
    @Override
    public void onSlashCommandInteraction(@NotNull SlashCommandInteractionEvent event) {
        Member member = event.getMember();
        if (event.getName().equals("nuke")) {
            if (!PermissionUtil.checkPermission(member, Permission.MANAGE_CHANNEL)) {
                event.reply("You dont have the permissions to access the command!").setEphemeral(true).queue();
            } else {
                MessageChannel channel = event.getOption("channel").getAsMessageChannel();
                assert channel != null;
                Objects.requireNonNull(event.getGuild()).getTextChannelsByName(channel.getName(), true).get(0).createCopy().queue();
                Objects.requireNonNull(event.getGuild()).getTextChannelsByName(channel.getName(), true).get(0).delete().queue();
            }
        }
    }
}
