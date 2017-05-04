import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { Story } from './story';
import { StoryService } from './story.service';

@Component({
  moduleId: module.id,
  selector: 'story-list',
  templateUrl: 'story-list.component.html',
  styleUrls: [ 'story-list.component.css']
})
export class StoryListComponent implements OnInit {
  stories: Story[];
  selectedStory: Story;

  constructor(
    private router: Router,
    private storyService: StoryService) { }

  getStories(): void {
    this.storyService.getStories().then(stories => this.stories = stories);
  }

  add(title: string): void {
   title = title.trim();
   if (!title) { return; }
   this.storyService.create(title)
     .then(story => {
       this.stories.push(story);
       this.selectedStory = null;
     });
 }

 delete(story: Story): void {
 this.storyService
     .delete(story.id)
     .then(() => {
       this.stories = this.stories.filter(s => s !== story);
       if (this.selectedStory === story) { this.selectedStory = null; }
     });
}

  ngOnInit(): void {
    this.getStories();
  }

  onSelect(story: Story): void {
    this.selectedStory = story;
  }

  gotoDetail(): void {
    this.router.navigate(['/story-editor', this.selectedStory.id]);
  }
}