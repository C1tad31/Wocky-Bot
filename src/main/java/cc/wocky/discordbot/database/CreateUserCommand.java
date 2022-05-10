package cc.wocky.discordbot.database;

import net.dv8tion.jda.api.Permission;
import net.dv8tion.jda.api.entities.Member;
import net.dv8tion.jda.api.events.interaction.command.SlashCommandInteractionEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

public class CreateUserCommand extends ListenerAdapter {
    public void onSlashCommand(SlashCommandInteractionEvent event) {
        Member member = event.getMember();
        if (event.getName().equals("create")) {
            if (!member.hasPermission(Permission.ADMINISTRATOR)) {
                event.reply("You dont have the required permission to use this command!").setEphemeral(true).queue();
            } else {
                
            }
        }
    }
}
