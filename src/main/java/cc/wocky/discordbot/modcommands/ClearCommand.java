package cc.wocky.discordbot.modcommands;

import net.dv8tion.jda.api.Permission;
import net.dv8tion.jda.api.entities.Member;
import net.dv8tion.jda.api.entities.Message;
import net.dv8tion.jda.api.entities.MessageChannel;
import net.dv8tion.jda.api.entities.MessageHistory;
import net.dv8tion.jda.api.events.interaction.command.SlashCommandInteractionEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
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

                MessageHistory history = new MessageHistory((MessageChannel) channel);
                List<Message> msg = history.retrievePast(amount).complete();

                event.getChannel().purgeMessages(msg);
            }
        }
    }
}
