package cc.wocky.discordbot.reputation;

import net.dv8tion.jda.api.entities.Member;

public class ReputationService {
    private Member member;
    private int repPoint;

    public Member getMember() {
        return member;
    }

    public void setMember(Member member) {
        this.member = member;
    }

    public int getRepPoint() {
        return repPoint;
    }

    public void setRepPoint(int repPoint) {
        this.repPoint = repPoint;
    }
}
