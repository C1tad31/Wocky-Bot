package cc.wocky.discordbot.reputation;

import net.dv8tion.jda.api.entities.Member;
import net.dv8tion.jda.api.entities.Role;
import net.dv8tion.jda.api.events.interaction.command.SlashCommandInteractionEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import org.jetbrains.annotations.NotNull;

public class ReputationCommand extends ListenerAdapter {

    private ReputationService reputationService = new ReputationService();

    @Override
    public void onSlashCommandInteraction(@NotNull SlashCommandInteractionEvent event) {
        Member member = event.getMember();
        if (event.getName().equals("rep")) {
            Role role = event.getGuild().getRolesByName("Verified", true).get(0);
            if (!member.getGuild().getRoles().contains(role)) {
                event.reply("You cannot use this command because you arent a verifed user yet!").setEphemeral(true).queue();
            } else {
                Member personToRep = event.getOption("member").getAsMember();
                Integer repPoints = event.getOption("num").getAsInt();


                if (repPoints <= 0) {
                    event.reply("Rep points must not be lower then 0!").setEphemeral(true).queue();
                } else if (repPoints >= 100) {
                    event.reply("You cant only give 100 rep points per user per command use!").setEphemeral(true).queue();
                } else {
                    // Logic Here
                }
            }
        }
    }
}
