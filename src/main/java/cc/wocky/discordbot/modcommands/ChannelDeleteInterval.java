package cc.wocky.discordbot.modcommands;

import net.dv8tion.jda.api.Permission;
import net.dv8tion.jda.api.entities.Member;
import net.dv8tion.jda.api.entities.MessageChannel;
import net.dv8tion.jda.api.events.interaction.command.SlashCommandInteractionEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import net.dv8tion.jda.internal.utils.PermissionUtil;
import org.jetbrains.annotations.NotNull;

import java.util.TimerTask;
import java.util.concurrent.TimeUnit;

public class ChannelDeleteInterval extends ListenerAdapter {
    @Override
    public void onSlashCommandInteraction(@NotNull SlashCommandInteractionEvent event) {
        Member member = event.getMember();
        if (event.getName().equals("autodelete")) {
            if (!PermissionUtil.checkPermission(member, Permission.ADMINISTRATOR)) {
                event.reply("You dont have the permissions to access the command!").setEphemeral(true).queue();
            } else {
                MessageChannel channel = event.getOption("channel").getAsMessageChannel();
                boolean running = true;
                while (running) {
                    TimerTask timerTask = new TimerTask() {
                        @Override
                        public void run() {
                            assert channel != null;
                            event.getGuild().getTextChannelsByName(channel.toString(), true).get(0).createCopy().queue();
                            event.getGuild().getTextChannelsByName(channel.toString(), true).get(0).delete().queueAfter(12, TimeUnit.HOURS);
                            event.reply("Channel has been purged due to security reasons!").queue();
                        }
                    };
                    timerTask.run();
                }
            }
        }
    }
}
