package cc.wocky.discordbot.modcommands;

import net.dv8tion.jda.api.Permission;
import net.dv8tion.jda.api.entities.Member;
import net.dv8tion.jda.api.entities.TextChannel;
import net.dv8tion.jda.api.events.interaction.command.SlashCommandInteractionEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import org.jetbrains.annotations.NotNull;

import java.util.Objects;

public class UnlockCommand extends ListenerAdapter {
    @Override
    public void onSlashCommandInteraction(@NotNull SlashCommandInteractionEvent event) {
        Member member = event.getMember();
        if (event.getName().equals("unlock")) {
            if (!member.hasPermission(Permission.MANAGE_PERMISSIONS) || !member.hasPermission(Permission.ADMINISTRATOR)) {
                event.reply("You dont have the required permission to use this command!").setEphemeral(true).queue();
            } else {
                TextChannel channel = (TextChannel) Objects.requireNonNull(event.getOption("channel")).getAsMessageChannel();
                assert channel != null;
                channel.getManager().putMemberPermissionOverride(member.getUser().getIdLong(),963279279997743164L, 963277437280612362L).queue();
                event.reply("Channel is unlocked!").queue();
            }
        }
    }
}
